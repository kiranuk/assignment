from sqlalchemy.orm import Session
from sqlalchemy.testing import db

from db.models.products import Product, Wine, WineNutritionalInfo
from schemas.products import WineUpdate


def create_wine(db, wine):
    product_data = wine.dict().pop('product', [])
    nutritional_info = wine.dict().pop('nutritional_info', {})
    wine_data = wine.dict(exclude={'product', 'nutritional_info'})
    wine = Wine(**wine_data)
    db.add(wine)
    db.commit()
    db.refresh(wine)
    nutritional_info = WineNutritionalInfo(**nutritional_info)
    nutritional_info.wine = wine
    nutritional_info.wine_id = wine.id
    db.add(nutritional_info)
    db.commit()
    db.refresh(nutritional_info)
    # Create Product objects associated with the wine
    for product_dict in product_data:
        product = Product(**product_dict)
        product.wine = wine
        product.wine_id = wine.id
        db.add(product)
        db.commit()
        db.refresh(product)
    db.commit()
    db.refresh(wine)
    return wine


def update_wine(
        db: Session, wine: Wine, wine_update: WineUpdate) -> Product:
    """
    Update the details of a product in the database.

    Args:
        db (Session): SQLAlchemy database session.
        db_product (Product): Product object retrieved from the database.
        product_update (WineUpdate): Updated product data.

    Returns:
        Product: Updated product object.
    """
    product_data = wine.dict().pop('product', [])
    wine_data = wine.dict(exclude={'product'})
    for field, value in wine_data.dict().items():
        setattr(wine, field, value)
    if product_data:
        db_product = db.query(Product).filter(Product.wine_id == wine.id).first()
        for product_dict in product_data:
            for field, value in product_dict.dict().items():
                setattr(db_product, field, value)
        db.commit()
        db.refresh(db_product)
    db.commit()
    # Refresh the product object to reflect the changes in the session
    db.refresh(wine)

    return wine
