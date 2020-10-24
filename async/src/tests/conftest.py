import pytest
from starlette.testclient import TestClient

from app.main import app

@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client


def test_ping(test_app):
    res = test_app.get("/ping")
    assert res.status_code == 200
    assert res.json == {"ping": "pong!"}
