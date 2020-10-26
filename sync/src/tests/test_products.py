import json
import pytest

from app.api import crud


def test_create_product(test_app, monkeypatch):
    data = {"name": "product 1", "description": "product 1 desc", "id": 1}

    def mock_post(db_session, payload):
        return data

    monkeypatch.setattr(crud, "post", mock_post)

    res = test_app.post("/products/", data=json.dumps(data),)
    assert res.status_code == 201
    assert res.json() == data


def test_create_product_invalid_json(test_app):
    res = test_app.post("/products/", data=json.dumps({"name": "product 1"}))
    assert res.status_code == 422

    res = test_app.post(
        "/products/", data=json.dumps({"name": "1", "description": "2"})
    )
    assert res.status_code == 422


def test_read_product(test_app, monkeypatch):
    data = {"name": "product 1", "description": "product 1 desc", "id": 1}

    def mock_get(db_session, id):
        return data

    monkeypatch.setattr(crud, "get", mock_get)

    res = test_app.get("/products/1")
    assert res.status_code == 200
    assert res.json() == data


def test_read_product_incorrect_id(test_app, monkeypatch):
    def mock_get(db_session, id):
        return None

    monkeypatch.setattr(crud, "get", mock_get)

    res = test_app.get("/products/999")
    assert res.status_code == 404
    assert res.json()["detail"] == "Product not found"

    res = test_app.get("/products/0")
    assert res.status_code == 422


def test_read_all_products(test_app, monkeypatch):
    data = [
        {"name": "product 1", "description": "product 1 desc", "id": 1},
        {"name": "product 2", "description": "product 2 desc", "id": 2},
    ]

    def mock_get_all(db_session):
        return data

    monkeypatch.setattr(crud, "get_all", mock_get_all)

    res = test_app.get("/products/")
    assert res.status_code == 200
    assert res.json() == data


def test_update_product(test_app, monkeypatch):
    data = {"name": "product 1", "description": "product 1 desc", "id": 1}
    update_data = {"name": "product 1 update", "description": "product 1 desc update", "id": 1}

    def mock_get(db_session, id):
        return data

    monkeypatch.setattr(crud, "get", mock_get)

    def mock_put(db_session, product, name, description):
        return update_data

    monkeypatch.setattr(crud, "put", mock_put)

    res = test_app.put("/products/1/", data=json.dumps(update_data),)
    assert res.status_code == 200
    assert res.json() == update_data


@pytest.mark.parametrize(
    "id, payload, status_code",
    [
        [1, {}, 422],
        [1, {"description": "bar"}, 422],
        [999, {"name": "foo", "description": "bar"}, 404],
        [1, {"name": "1", "description": "bar"}, 422],
        [1, {"name": "foo", "description": "1"}, 422],
        [0, {"name": "foo", "description": "bar"}, 422],
    ],
)
def test_update_product_invalid(test_app, monkeypatch, id, payload, status_code):
    def mock_get(db_session, id):
        return None

    monkeypatch.setattr(crud, "get", mock_get)

    res = test_app.put(f"/products/{id}/", data=json.dumps(payload),)
    assert res.status_code == status_code


def test_remove_product(test_app, monkeypatch):
    data = {"name": "product 1", "description": "product 1 desc", "id": 1}

    def mock_get(db_session, id):
        return data

    monkeypatch.setattr(crud, "get", mock_get)

    def mock_delete(db_session, id):
        return data

    monkeypatch.setattr(crud, "delete", mock_delete)

    res = test_app.delete("/products/1/")
    assert res.status_code == 200
    assert res.json() == data


def test_remove_product_incorrect_id(test_app, monkeypatch):
    def mock_get(db_session, id):
        return None

    monkeypatch.setattr(crud, "get", mock_get)

    res = test_app.delete("/products/999/")
    assert res.status_code == 404
    assert res.json()["detail"] == "Product not found"

    res = test_app.delete("/products/0/")
    assert res.status_code == 422