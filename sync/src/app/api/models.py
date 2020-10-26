from pydantic import BaseModel, Field
from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, String, DateTime

from app.db import Base


class Product(Base):

    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(String(50))
    created_date = Column(DateTime, default=func.now(), nullable=False)

    def __init__(self, name, description):
        self.name = name
        self.description = description


class ProductSchema(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    description: str = Field(..., min_length=3, max_length=50)


class ProductDB(ProductSchema):
    id: int

    class Config:
        orm_mode = True