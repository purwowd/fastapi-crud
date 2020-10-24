from fastapi import FastAPI
import uvicorn

from app.api import ping, products
from app.db import engine, metadata, database


metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(ping.router)
app.include_router(products.router, prefix="/products", tags=["products"])


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
