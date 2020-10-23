import os

from databases import Database
from sqlalchemy import (create_engine, MetaData, Column, DateTime,
                        Integer, String, Table)
from sqlalchemy.sql import func


DATABASE_URL = "postgresql://postgres:dev@127.0.0.1/async_crud_fastapi"

engine = create_engine(DATABASE_URL)
metadata = MetaData()
products = Table(
    "products",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
    Column("description", String(50)),
    Column("created_date", DateTime, default=func.now(), nullable=False),
)

database = Database(DATABASE_URL)
