from pydantic import BaseModel
from typing import Dict, Any, List

class ServiceHealth(BaseModel):
    status: str
    service: str
    port: int
    response: Dict[str, Any] = None
    error: str = None

class ServiceInfo(BaseModel):
    url: str
    port: int
    description: str

class ServicesResponse(BaseModel):
    gateway: ServiceInfo
    auth: ServiceInfo
    materiality: ServiceInfo
    gri: ServiceInfo
    tcfd: ServiceInfo
    chatbot: ServiceInfo

class GatewayResponse(BaseModel):
    message: str
    port: int
    services: List[str]
