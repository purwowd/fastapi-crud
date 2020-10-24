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