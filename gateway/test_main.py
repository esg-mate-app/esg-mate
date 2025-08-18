import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    """루트 엔드포인트 테스트"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "ESG Mate Gateway"
    assert data["port"] == 8080

def test_health():
    """헬스체크 엔드포인트 테스트"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["service"] == "gateway"
    assert data["port"] == 8080

def test_services():
    """서비스 정보 엔드포인트 테스트"""
    response = client.get("/services")
    assert response.status_code == 200
    data = response.json()
    assert "gateway" in data
    assert "auth" in data
    assert "materiality" in data
    assert "gri" in data
    assert "tcfd" in data
    assert "chatbot" in data
