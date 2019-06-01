import pytest

from app import create_app


@pytest.fixture
def client():
    application = create_app()
    client = application.test_client()
    yield client


def test_routes(client):
    response = client.get("/")
    assert response.status_code == 200
    response = client.get("/invalid")
    assert response.status_code == 404
