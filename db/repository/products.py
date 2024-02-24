from sqlalchemy.orm import Session
from sqlalchemy.testing import db

from db.models.products import Product


def create_product(product_dict):
    product = Product(**product_dict)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product