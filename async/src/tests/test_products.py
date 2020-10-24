import json
import pytest

from app.api import crud


def test_create_product(test_app, monkeypatch):
    request_payload = {"name": "sample product", "description": "sample desc"}
    response_payload = {"id": 1, "name": "sample product", "description": "sample desc"}

    async def mock_post(payload):
        print(payload)
        return 1

    monkeypatch.setattr(crud, "post", mock_post)
    res = test_app.post("/products/", data=json.dumps(request_payload),)

    assert res.status_code == 201
    assert res.json() == response_payload


def test_create_product_invalid_json(test_app):
    res = test_app.post("/products/", data=json.dumps({"name": "sample product"}))
    assert res.status_code == 422


def test_read_product(test_app, monkeypatch):
    test_data = {"id": 1, "name": "sample product", "description": "sample product desc"}

    async def mock_get(id):
        print(id)
        return test_data

    monkeypatch.setattr(crud, "get", mock_get)

    res = test_app.get("/products/1")
    assert res.status_code == 200
    assert res.json() == test_data


def test_read_product_incorrect_id(test_app, monkeypatch):
    async def mock_get(id):
        print(id)
        return None

    monkeypatch.setattr(crud, "get", mock_get)

    res = test_app.get("/products/99")
    assert res.status_code == 404
    assert res.json()["detail"] == "Product not found"
