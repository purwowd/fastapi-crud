from fastapi import APIRouter, HTTPException
from typing import List

from app.api import crud
from app.api.models import ProductSchema, ProductDB


router = APIRouter()


@router.post("/", response_model=ProductDB, status_code=201)
async def create_product(payload: ProductSchema):
    product_id = await crud.post(payload)

    response_object = {
        "id": product_id,
        "name": payload.name,
        "description": payload.description,
    }
    return response_object


@router.get("/{id}/", response_model=ProductDB)
async def read_product(id: int):
    product = await crud.get(id)

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.get("/", response_model=List[ProductDB])
async def read_all_product():
    return await crud.get_all()


@router.put("/{id}/", response_model=ProductDB)
async def update_product(id: int, payload: ProductSchema):
    product = await crud.get(id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    product_id = await crud.put(id, payload)

    res_object = {
        "id": product_id,
        "name": payload.name,
        "description": payload.description,
    }

    return res_object


@router.delete("/{id}/", response_model=ProductDB)
async def delete_product(id: int):
    product = await crud.get(id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    await crud.delete(id)

    return product