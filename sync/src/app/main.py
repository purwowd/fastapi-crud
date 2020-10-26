from fastapi import FastAPI
import uvicorn

from app.db import engine
from app.api import ping, products
from app.api.models import Base


Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(ping.router)
app.include_router(products.router, prefix="/products", tags=["products"])


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)