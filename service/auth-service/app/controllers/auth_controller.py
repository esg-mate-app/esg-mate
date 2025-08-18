from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import List
from ..models.user_models import (
    UserCreate, UserLogin, UserResponse, TokenResponse, 
    UserUpdate, PasswordChange
)
from ..services.auth_service import AuthService
from ..services.jwt_service import JWTService

router = APIRouter()
security = HTTPBearer()

# 서비스 인스턴스
auth_service = AuthService()
jwt_service = JWTService()

@router.get("/", response_model=dict)
async def root():
    """Auth Service 루트 엔드포인트"""
    return {
        "message": "Auth Service",
        "port": 8008,
        "endpoints": ["/login", "/register", "/verify", "/health", "/users"]
    }

@router.get("/health")
async def health_check():
    """Auth Service 헬스체크"""
    return {
        "status": "healthy",
        "service": "auth",
        "port": 8008
    }

@router.post("/register", response_model=UserResponse)
async def register(user_data: UserCreate):
    """사용자 등록"""
    try:
        user = await auth_service.create_user(user_data)
        return user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")

@router.post("/login", response_model=TokenResponse)
async def login(user_data: UserLogin):
    """사용자 로그인"""
    try:
        user = await auth_service.authenticate_user(user_data.username, user_data.password)
        if not user:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        
        token = jwt_service.create_access_token(user)
        return TokenResponse(
            access_token=token,
            token_type="bearer",
            expires_in=3600,
            user=user
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/verify")
async def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """토큰 검증"""
    try:
        payload = jwt_service.verify_token(credentials.credentials)
        user = await auth_service.get_user_by_id(payload.get("user_id"))
        if not user:
            raise HTTPException(status_code=401, detail="User not found")
        
        return {
            "valid": True,
            "user": user
        }
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid token")

@router.get("/users", response_model=List[UserResponse])
async def get_users():
    """모든 사용자 조회 (관리자용)"""
    try:
        users = await auth_service.get_all_users()
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")

@router.put("/users/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user_data: UserUpdate):
    """사용자 정보 수정"""
    try:
        user = await auth_service.update_user(user_id, user_data)
        return user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")

@router.post("/users/{user_id}/change-password")
async def change_password(user_id: int, password_data: PasswordChange):
    """비밀번호 변경"""
    try:
        success = await auth_service.change_password(
            user_id, 
            password_data.current_password, 
            password_data.new_password
        )
        if success:
            return {"message": "Password changed successfully"}
        else:
            raise HTTPException(status_code=400, detail="Current password is incorrect")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
