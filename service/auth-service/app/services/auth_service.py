from typing import List, Optional
from passlib.context import CryptContext
from ..models.user_models import UserCreate, UserResponse, UserUpdate
from ..repositories.user_repository import UserRepository

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AuthService:
    """인증 및 사용자 관리 서비스"""
    
    def __init__(self):
        self.user_repository = UserRepository()
    
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """비밀번호 검증"""
        return pwd_context.verify(plain_password, hashed_password)
    
    def get_password_hash(self, password: str) -> str:
        """비밀번호 해시화"""
        return pwd_context.hash(password)
    
    async def create_user(self, user_data: UserCreate) -> UserResponse:
        """사용자 생성"""
        # 사용자명 중복 확인
        existing_user = await self.user_repository.get_user_by_username(user_data.username)
        if existing_user:
            raise ValueError("Username already exists")
        
        # 이메일 중복 확인
        existing_email = await self.user_repository.get_user_by_email(user_data.email)
        if existing_email:
            raise ValueError("Email already exists")
        
        # 비밀번호 해시화
        hashed_password = self.get_password_hash(user_data.password)
        
        # 사용자 생성
        user = await self.user_repository.create_user(
            username=user_data.username,
            email=user_data.email,
            hashed_password=hashed_password,
            role="user"
        )
        
        return user
    
    async def authenticate_user(self, username: str, password: str) -> Optional[UserResponse]:
        """사용자 인증"""
        user = await self.user_repository.get_user_by_username(username)
        if not user:
            return None
        
        if not self.verify_password(password, user.hashed_password):
            return None
        
        return user
    
    async def get_user_by_id(self, user_id: int) -> Optional[UserResponse]:
        """ID로 사용자 조회"""
        return await self.user_repository.get_user_by_id(user_id)
    
    async def get_all_users(self) -> List[UserResponse]:
        """모든 사용자 조회"""
        return await self.user_repository.get_all_users()
    
    async def update_user(self, user_id: int, user_data: UserUpdate) -> UserResponse:
        """사용자 정보 수정"""
        user = await self.user_repository.get_user_by_id(user_id)
        if not user:
            raise ValueError("User not found")
        
        update_data = {}
        if user_data.email is not None:
            # 이메일 중복 확인
            existing_email = await self.user_repository.get_user_by_email(user_data.email)
            if existing_email and existing_email.id != user_id:
                raise ValueError("Email already exists")
            update_data["email"] = user_data.email
        
        if user_data.password is not None:
            update_data["hashed_password"] = self.get_password_hash(user_data.password)
        
        if user_data.role is not None:
            update_data["role"] = user_data.role
        
        updated_user = await self.user_repository.update_user(user_id, update_data)
        return updated_user
    
    async def change_password(self, user_id: int, current_password: str, new_password: str) -> bool:
        """비밀번호 변경"""
        user = await self.user_repository.get_user_by_id(user_id)
        if not user:
            return False
        
        if not self.verify_password(current_password, user.hashed_password):
            return False
        
        hashed_new_password = self.get_password_hash(new_password)
        await self.user_repository.update_user(user_id, {"hashed_password": hashed_new_password})
        return True
