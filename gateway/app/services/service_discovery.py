import httpx
import os
from typing import Dict, Any, List
from ..models.service_models import ServiceHealth

class ServiceDiscoveryService:
    """서비스 디스커버리 및 헬스체크 서비스"""
    
    def __init__(self):
        self.service_urls = {
            "gateway": os.getenv("GATEWAY_SERVICE_URL", "http://localhost:8080"),
            "materiality": os.getenv("MATERIALITY_SERVICE_URL", "http://localhost:8002"),
            "gri": os.getenv("GRI_SERVICE_URL", "http://localhost:8003"),
            "tcfd": os.getenv("TCFD_SERVICE_URL", "http://localhost:8005"),
            "chatbot": os.getenv("CHATBOT_SERVICE_URL", "http://localhost:8001"),
            "auth": os.getenv("AUTH_SERVICE_URL", "http://localhost:8008")
        }
    
    async def check_service_health(self, service_name: str, service_url: str) -> ServiceHealth:
        """개별 서비스 헬스체크"""
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(f"{service_url}/health", timeout=5.0)
                port = int(service_url.split(":")[-1].split("/")[0]) if ":" in service_url else 0
                return ServiceHealth(
                    status="healthy",
                    service=service_name,
                    port=port,
                    response=response.json()
                )
        except Exception as e:
            port = int(service_url.split(":")[-1].split("/")[0]) if ":" in service_url else 0
            return ServiceHealth(
                status="unhealthy",
                service=service_name,
                port=port,
                error=str(e)
            )
    
    async def check_all_services_health(self) -> Dict[str, ServiceHealth]:
        """모든 서비스 헬스체크"""
        health_status = {}
        
        for service_name, service_url in self.service_urls.items():
            health_status[service_name] = await self.check_service_health(service_name, service_url)
        
        return health_status
    
    def get_service_urls(self) -> Dict[str, str]:
        """등록된 서비스 URL 반환"""
        return self.service_urls
    
    def get_service_info(self) -> Dict[str, Dict[str, Any]]:
        """서비스 정보 반환"""
        service_info = {}
        for service_name, service_url in self.service_urls.items():
            port = int(service_url.split(":")[-1].split("/")[0]) if ":" in service_url else 0
            service_info[service_name] = {
                "url": service_url,
                "port": port,
                "description": self._get_service_description(service_name)
            }
        return service_info
    
    def _get_service_description(self, service_name: str) -> str:
        """서비스 설명 반환"""
        descriptions = {
            "gateway": "API Gateway Service",
            "auth": "Authentication Service",
            "materiality": "Materiality Assessment Service",
            "gri": "GRI Standards Service",
            "tcfd": "TCFD Framework Service",
            "chatbot": "AI Chatbot Service"
        }
        return descriptions.get(service_name, "Unknown Service")
