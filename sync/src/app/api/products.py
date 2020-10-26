from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Path

from app.db import SessionLocal
from app.api import crud
from app.api.models import ProductDB, ProductSchema


router = APIRouter()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@router.post("/", response_model=ProductDB, status_code=201)
def create_product(*, db: Session = Depends(get_db), payload: ProductSchema):
    product = crud.post(db_session=db, payload=payload)
    return product


@router.get("/{id}/", response_model=ProductDB)
def read_product(
    *, db: Session = Depends(get_db), id: int = Path(..., gt=0),
):
    product = crud.get(db_session=db, id=id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.get("/", response_model=List[ProductDB])
def read_all_products(db: Session = Depends(get_db)):
    return crud.get_all(db_session=db)


@router.put("/{id}/", response_model=ProductDB)
def update_product(
    *, db: Session = Depends(get_db), id: int = Path(..., gt=0), payload: ProductSchema
):
    product = crud.get(db_session=db, id=id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    product = crud.put(
        db_session=db, product=product, name=payload.name, description=payload.description
    )
    return product


@router.delete("/{id}/", response_model=ProductDB)
def delete_product(
    *, db: Session = Depends(get_db), id: int = Path(..., gt=0),
):
    product = crud.get(db_session=db, id=id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    product = crud.delete(db_session=db, id=id)
    return product