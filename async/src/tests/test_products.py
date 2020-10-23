import json
import pytest

from app.api import crud


def test_create_product(test_app, monkeypatch):
    request_payload = {"name": "sample product", "description": "sample desc"}
    response_payload = {"id": 1, "name": "sample product", "description": "sample desc"}

    async def mock_post(payload):
        return 1

    monkeypatch.setattr(crud, "post", mock_post)
    res = test_app.post("/products/", data=json.dumps(request_payload),)

    assert res.status_code == 201
    assert res.json() == response_payload


def test_create_product_invalid_json(test_app):
    res = test_app.post("/products/", data=json.dumps({"name": "sample product"}))
    assert res.status_code == 422
