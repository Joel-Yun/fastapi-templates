import sys
import os

# NOTE: src 폴더를 경로에 추가
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_ping():
    """
    NOTE: '/api/ping' 엔드포인트 테스트
    """

    response = client.get("/api/ping")

    assert response.status_code == 200
    assert response.json() == {"message": "pong"}
