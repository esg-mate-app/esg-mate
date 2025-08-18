import os
from typing import List

class Settings:
    """Auth Service 설정"""
    
    # 기본 설정
    APP_NAME: str = "Auth Service"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    
    # 서버 설정
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", 8008))
    
    # JWT 설정
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "your-secret-key-here")
    JWT_ALGORITHM: str = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRE_MINUTES", "60"))
    
    # 보안 설정
    PASSWORD_MIN_LENGTH: int = int(os.getenv("PASSWORD_MIN_LENGTH", "8"))
    PASSWORD_REQUIRE_SPECIAL_CHAR: bool = os.getenv("PASSWORD_REQUIRE_SPECIAL_CHAR", "True").lower() == "true"
    
    # 데이터베이스 설정 (향후 확장용)
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./auth.db")
    
    # CORS 설정
    ALLOWED_ORIGINS: List[str] = ["*"]  # 개발 환경용
    
    # 로깅 설정
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

# 전역 설정 인스턴스
settings = Settings()
