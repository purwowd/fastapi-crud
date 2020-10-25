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


def test_read_all_product(test_app, monkeypatch):
    data = [
        {"name": "product 1", "description": "product desc 1", "id": 1},
        {"name": "product 2", "description": "product desc 2", "id": 2},
    ]

    async def mock_get_all():
        return data

    monkeypatch.setattr(crud, "get_all", mock_get_all)

    res = test_app.get("/products/")
    assert res.status_code == 200
    assert res.json() == data


def test_update_product(test_app, monkeypatch):
    data = {"name": "product 1", "description": "product desc 1", "id": 1}

    async def mock_get(id):
        print(id)
        return True

    monkeypatch.setattr(crud, "get", mock_get)

    async def mock_put(id, payload):
        print(id)
        print(payload)
        return 1

    monkeypatch.setattr(crud, "put", mock_put)
    res = test_app.put("/products/1/", data=json.dumps(data))

    assert res.status_code == 200
    assert res.json() == data


@pytest.mark.parametrize(
    "id, payload, status_code",
    [
        [1, {}, 422],
        [1, {"description": "bar"}, 422],
        [999, {"name": "foo", "description": "bar"}, 404],
    ],
)
def test_update_product_invalid(test_app, monkeypatch, id, payload, status_code):
    async def mock_get(id):
        print(id)
        return None

    monkeypatch.setattr(crud, "get", mock_get)

    res = test_app.put(f"/products/{id}/", data=json.dumps(payload),)
    assert res.status_code == status_code


def test_delete_product(test_app, monkeypatch):
    data = {"name": "product 1", "description": "product 1 desc", "id": 1}

    async def mock_get(id):
        print(id)
        return data

    monkeypatch.setattr(crud, "get", mock_get)

    async def mock_delete(id):
        print(id)

    monkeypatch.setattr(crud, "delete", mock_delete)

    res = test_app.delete("/products/1/")
    assert res.status_code == 200
    assert res.json() == data


def test_delete_product_incorret_id(test_app, monkeypatch):
    async def mock_get(id):
        print(id)
        return None

    monkeypatch.setattr(crud, "get", mock_get)

    res = test_app.delete("/products/999/")
    assert res.status_code == 404
    assert res.json()["detail"] == "Product not found"
