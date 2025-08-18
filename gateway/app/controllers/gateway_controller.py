from fastapi import APIRouter, HTTPException
from typing import Dict, Any
import httpx
import os
from ..models.service_models import ServiceHealth, ServiceInfo, ServicesResponse, GatewayResponse

router = APIRouter()

# 서비스 URL 환경 변수
SERVICE_URLS = {
    "gateway": os.getenv("GATEWAY_SERVICE_URL", "http://localhost:8080"),
    "materiality": os.getenv("MATERIALITY_SERVICE_URL", "http://localhost:8002"),
    "gri": os.getenv("GRI_SERVICE_URL", "http://localhost:8003"),
    "tcfd": os.getenv("TCFD_SERVICE_URL", "http://localhost:8005"),
    "chatbot": os.getenv("CHATBOT_SERVICE_URL", "http://localhost:8001"),
    "auth": os.getenv("AUTH_SERVICE_URL", "http://localhost:8008")
}

@router.get("/", response_model=GatewayResponse)
async def root():
    """Gateway 루트 엔드포인트"""
    return GatewayResponse(
        message="ESG Mate Gateway",
        port=8080,
        services=list(SERVICE_URLS.keys())
    )

@router.get("/health")
async def health_check():
    """Gateway 헬스체크"""
    return {
        "status": "healthy",
        "service": "gateway",
        "port": 8080
    }

@router.get("/health/all")
async def check_all_services():
    """모든 서비스의 상태를 확인"""
    health_status = {}
    
    for service_name, service_url in SERVICE_URLS.items():
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(f"{service_url}/health", timeout=5.0)
                health_status[service_name] = ServiceHealth(
                    status="healthy",
                    service=service_name,
                    port=int(service_url.split(":")[-1].split("/")[0]),
                    response=response.json()
                )
        except Exception as e:
            health_status[service_name] = ServiceHealth(
                status="unhealthy",
                service=service_name,
                port=int(service_url.split(":")[-1].split("/")[0]) if ":" in service_url else 0,
                error=str(e)
            )
    
    return health_status

@router.get("/services", response_model=ServicesResponse)
async def get_services():
    """등록된 모든 서비스 정보 반환"""
    return ServicesResponse(
        gateway=ServiceInfo(
            url=SERVICE_URLS["gateway"],
            port=8080,
            description="API Gateway Service"
        ),
        auth=ServiceInfo(
            url=SERVICE_URLS["auth"],
            port=8008,
            description="Authentication Service"
        ),
        materiality=ServiceInfo(
            url=SERVICE_URLS["materiality"],
            port=8002,
            description="Materiality Assessment Service"
        ),
        gri=ServiceInfo(
            url=SERVICE_URLS["gri"],
            port=8003,
            description="GRI Standards Service"
        ),
        tcfd=ServiceInfo(
            url=SERVICE_URLS["tcfd"],
            port=8005,
            description="TCFD Framework Service"
        ),
        chatbot=ServiceInfo(
            url=SERVICE_URLS["chatbot"],
            port=8001,
            description="AI Chatbot Service"
        )
    )
