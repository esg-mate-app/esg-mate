from typing import List, Optional, Dict, Any
from ..models.user_models import UserResponse
from datetime import datetime

class UserRepository:
    """사용자 데이터 접근 리포지토리"""
    
    def __init__(self):
        # 실제 구현에서는 데이터베이스 연결을 사용
        # 현재는 메모리 기반 임시 구현
        self.users = [
            {
                "id": 1,
                "username": "admin",
                "email": "admin@esgmate.com",
                "hashed_password": "$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj4J/8QqJqG",  # "password"
                "role": "admin",
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow()
            }
        ]
        self.next_id = 2
    
    async def create_user(self, username: str, email: str, hashed_password: str, role: str = "user") -> UserResponse:
        """사용자 생성"""
        user_data = {
            "id": self.next_id,
            "username": username,
            "email": email,
            "hashed_password": hashed_password,
            "role": role,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        }
        
        self.users.append(user_data)
        self.next_id += 1
        
        return UserResponse(**user_data)
    
    async def get_user_by_id(self, user_id: int) -> Optional[UserResponse]:
        """ID로 사용자 조회"""
        for user in self.users:
            if user["id"] == user_id:
                return UserResponse(**user)
        return None
    
    async def get_user_by_username(self, username: str) -> Optional[UserResponse]:
        """사용자명으로 사용자 조회"""
        for user in self.users:
            if user["username"] == username:
                return UserResponse(**user)
        return None
    
    async def get_user_by_email(self, email: str) -> Optional[UserResponse]:
        """이메일로 사용자 조회"""
        for user in self.users:
            if user["email"] == email:
                return UserResponse(**user)
        return None
    
    async def get_all_users(self) -> List[UserResponse]:
        """모든 사용자 조회"""
        return [UserResponse(**user) for user in self.users]
    
    async def update_user(self, user_id: int, update_data: Dict[str, Any]) -> UserResponse:
        """사용자 정보 수정"""
        for i, user in enumerate(self.users):
            if user["id"] == user_id:
                # 업데이트할 필드들만 수정
                for key, value in update_data.items():
                    if key in user:
                        user[key] = value
                
                user["updated_at"] = datetime.utcnow()
                return UserResponse(**user)
        
        raise ValueError("User not found")
    
    async def delete_user(self, user_id: int) -> bool:
        """사용자 삭제"""
        for i, user in enumerate(self.users):
            if user["id"] == user_id:
                del self.users[i]
                return True
        return False
    
    async def get_users_by_role(self, role: str) -> List[UserResponse]:
        """역할별 사용자 조회"""
        return [UserResponse(**user) for user in self.users if user["role"] == role]
