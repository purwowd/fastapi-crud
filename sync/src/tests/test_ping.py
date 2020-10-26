from starlette.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_ping(test_app):
    res = test_app.get("/ping")
    assert res.status_code == 200
    assert res.json() == {"ping": "pong!"}