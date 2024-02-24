from http.client import HTTPException

from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from sqlalchemy.orm.exc import UnmappedInstanceError

from db.models.products import Product
from db.repository.products import update_product
from schemas.products import ProductCreate, ProductUpdate
from db.session import get_db

router = APIRouter()


@router.post("/")
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    product = Product(
        name=product.name, description=product.description)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


@router.get("/list")
def get_products(db: Session = Depends(get_db)):
    products = db.query(Product).all()
    return products


# get the product details with id
@router.get("/{id}")
def get_product(id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == id).first()
    return product


@router.patch("/{id}")
def update_product_details(
        id: int, product_update: ProductUpdate, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    db_product = update_product(db, product, product_update)
    return db_product


@router.delete("/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    try:
        product = db.query(Product).filter(Product.id == id).first()
    except UnmappedInstanceError:
        raise HTTPException(status_code=400, detail="Product not found")
    db.delete(product)
    db.commit()
    return {"message": "Product deleted successfully"}