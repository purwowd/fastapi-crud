from app.db import products, database
from app.api.models import ProductSchema


async def post(payload: ProductSchema):
    query = products.insert().values(name=payload.name, description=payload.description)
    return await database.execute(query=query)
