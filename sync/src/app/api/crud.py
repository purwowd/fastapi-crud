from sqlalchemy.orm import Session

from app.api.models import Product, ProductSchema


def post(db_session: Session, payload: ProductSchema):
    product = Product(name=payload.name, description=payload.description)
    db_session.add(product)
    db_session.commit()
    db_session.refresh(product)
    return product


def get(db_session: Session, id: int):
    return db_session.query(Product).filter(Product.id == id).first()


def get_all(db_session: Session):
    return db_session.query(Product).all()


def put(db_session: Session, product: Product, name: str, description: str):
    product.name = name
    product.description = description
    db_session.commit()
    return product


def delete(db_session: Session, id: int):
    product = db_session.query(Product).filter(Product.id == id).first()
    db_session.delete(product)
    db_session.commit()
    return product