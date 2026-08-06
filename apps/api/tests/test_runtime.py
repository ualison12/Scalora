from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root_health_endpoint() -> None:
    response = client.get("/")

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "running"
    assert payload["name"] == "Scalora API"


def test_cors_headers_are_present() -> None:
    response = client.options(
        "/",
        headers={
            "Origin": "http://localhost:3000",
            "Access-Control-Request-Method": "GET",
        },
    )

    assert response.status_code == 200
    assert "access-control-allow-origin" in response.headers
