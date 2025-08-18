import os
from typing import List

class Settings:
    """Gateway 서비스 설정"""
    
    # 기본 설정
    APP_NAME: str = "ESG Mate Gateway"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    
    # 서버 설정
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", 8080))
    
    # CORS 설정
    ALLOWED_ORIGINS: List[str] = [
        "https://your-frontend.vercel.app",
        "http://localhost:3000",
        "*"  # 개발 환경용
    ]
    
    # 서비스 URL 설정
    GATEWAY_SERVICE_URL: str = os.getenv("GATEWAY_SERVICE_URL", "http://localhost:8080")
    MATERIALITY_SERVICE_URL: str = os.getenv("MATERIALITY_SERVICE_URL", "http://localhost:8002")
    GRI_SERVICE_URL: str = os.getenv("GRI_SERVICE_URL", "http://localhost:8003")
    TCFD_SERVICE_URL: str = os.getenv("TCFD_SERVICE_URL", "http://localhost:8005")
    CHATBOT_SERVICE_URL: str = os.getenv("CHATBOT_SERVICE_URL", "http://localhost:8001")
    AUTH_SERVICE_URL: str = os.getenv("AUTH_SERVICE_URL", "http://localhost:8008")
    
    # 타임아웃 설정
    SERVICE_TIMEOUT: int = int(os.getenv("SERVICE_TIMEOUT", 5))
    
    @classmethod
    def get_service_urls(cls) -> dict:
        """서비스 URL 딕셔너리 반환"""
        return {
            "gateway": cls.GATEWAY_SERVICE_URL,
            "materiality": cls.MATERIALITY_SERVICE_URL,
            "gri": cls.GRI_SERVICE_URL,
            "tcfd": cls.TCFD_SERVICE_URL,
            "chatbot": cls.CHATBOT_SERVICE_URL,
            "auth": cls.AUTH_SERVICE_URL
        }

# 전역 설정 인스턴스
settings = Settings()
