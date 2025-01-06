""" Testing main.py """
from fastapi.testclient import TestClient
from app.main import app
from app.models.api_health import ApiHealth

client = TestClient(
    app=app,
    follow_redirects=False,
    root_path="/v0"
)


def test_api_health_check():
    """ Test add an expense. """
    response = client.get("/api/health")
    assert response.status_code == 200
    ApiHealth.model_validate(response.json())