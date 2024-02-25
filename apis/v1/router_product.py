from http.client import HTTPException
from typing import List

from fastapi import APIRouter, UploadFile
from fastapi.params import File
from sqlalchemy.orm import Session, joinedload
from fastapi import Depends
from sqlalchemy.orm.exc import UnmappedInstanceError

from db.models.products import Wine
from db.repository.wines import update_wine, create_wine
from schemas.products import WineCreate, WineUpdate, WineOutDBBase
from db.session import get_db

router = APIRouter()


@router.post("/", response_model=WineOutDBBase)
def create_wine_router(wine: WineCreate, db: Session = Depends(get_db)):
    wine = create_wine(db, wine)
    return wine


@router.get("/", response_model=List[WineOutDBBase])
def get_wines(db: Session = Depends(get_db)):
    wines = db.query(Wine).options(
        joinedload(Wine.products), joinedload(Wine.nutritional_info)).all()
    return wines


# get the product details with id
@router.get("/{id}", response_model=WineOutDBBase)
def get_wine(id: int, db: Session = Depends(get_db)):
    product = db.query(Wine).filter(Wine.id == id).first()
    return product


@router.patch("/{id}", response_model=WineOutDBBase)
def update_wine_details(
        id: int, wine_update: WineUpdate, db: Session = Depends(get_db)):
    wine = db.query(Wine).filter(Wine.id == id).first()
    if wine is None:
        raise HTTPException(status_code=404, detail="Product not found")
    db_product = update_wine(db, wine, wine_update)
    return db_product


@router.delete("/{id}")
def delete_wine(id: int, db: Session = Depends(get_db)):
    try:
        wine = db.query(Wine).filter(Wine.id == id).first()
    except UnmappedInstanceError:
        raise HTTPException(status_code=400, detail="Product not found")
    db.delete(wine)
    db.commit()
    return {"message": "Wine deleted successfully"}


@router.patch("/{id}/image", response_model=WineOutDBBase)
def update_wine_image(id: int, image: UploadFile = File(...), db: Session = Depends(get_db)):
    wine = db.query(Wine).filter(Wine.id == id).first()
    wine.image = wine.save_image_to_s3(image)
    db.commit()
    db.refresh(wine)
    return wine

