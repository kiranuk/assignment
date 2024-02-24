from sqlalchemy.orm import Session
from sqlalchemy.testing import db

from db.models.products import Product
from schemas.products import ProductUpdate


def create_product(product):
    product = Product(
        name=product.name, description=product.description)
    db.add(product)
    db.commit()
    db.refresh(product)


def update_product(
        db: Session, db_product: Product, product_update: ProductUpdate) -> Product:
    """
    Update the details of a product in the database.

    Args:
        db (Session): SQLAlchemy database session.
        db_product (Product): Product object retrieved from the database.
        product_update (ProductUpdate): Updated product data.

    Returns:
        Product: Updated product object.
    """
    # Update the product details with the new values
    for field, value in product_update.dict().items():
        setattr(db_product, field, value)

    # Commit the changes to the database
    db.commit()

    # Refresh the product object to reflect the changes in the session
    db.refresh(db_product)

    return db_product
