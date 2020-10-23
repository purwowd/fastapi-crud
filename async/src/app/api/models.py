from pydantic import BaseModel


class ProductSchema(BaseModel):
    name: str
    description: str


class ProductDB(ProductSchema):
    id: int
