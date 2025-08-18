from datetime import datetime, timedelta
from typing import Optional, Dict, Any
from jose import JWTError, jwt
from ..models.user_models import UserResponse
import os

class JWTService:
    """JWT 토큰 관리 서비스"""
    
    def __init__(self):
        self.secret_key = os.getenv("JWT_SECRET_KEY", "your-secret-key-here")
        self.algorithm = "HS256"
        self.access_token_expire_minutes = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRE_MINUTES", "60"))
    
    def create_access_token(self, user: UserResponse) -> str:
        """액세스 토큰 생성"""
        expire = datetime.utcnow() + timedelta(minutes=self.access_token_expire_minutes)
        
        to_encode = {
            "sub": str(user.id),
            "user_id": user.id,
            "username": user.username,
            "email": user.email,
            "role": user.role,
            "exp": expire
        }
        
        encoded_jwt = jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)
        return encoded_jwt
    
    def verify_token(self, token: str) -> Dict[str, Any]:
        """토큰 검증 및 디코딩"""
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return payload
        except JWTError:
            raise ValueError("Invalid token")
    
    def get_user_id_from_token(self, token: str) -> Optional[int]:
        """토큰에서 사용자 ID 추출"""
        try:
            payload = self.verify_token(token)
            return payload.get("user_id")
        except ValueError:
            return None
    
    def is_token_expired(self, token: str) -> bool:
        """토큰 만료 여부 확인"""
        try:
            payload = self.verify_token(token)
            exp = payload.get("exp")
            if exp is None:
                return True
            
            expire_datetime = datetime.fromtimestamp(exp)
            return datetime.utcnow() > expire_datetime
        except ValueError:
            return True
    
    def refresh_token(self, token: str) -> Optional[str]:
        """토큰 갱신"""
        try:
            payload = self.verify_token(token)
            if self.is_token_expired(token):
                return None
            
            # 새로운 만료 시간으로 토큰 재생성
            user_data = {
                "id": payload.get("user_id"),
                "username": payload.get("username"),
                "email": payload.get("email"),
                "role": payload.get("role")
            }
            
            user = UserResponse(**user_data)
            return self.create_access_token(user)
        except ValueError:
            return None
