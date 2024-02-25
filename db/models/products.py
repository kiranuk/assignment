from datetime import datetime

from fastapi import UploadFile
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import Float
from sqlalchemy.orm import relationship

from core.config import settings
from db.base_class import Base


class Wine(Base):

    __tablename__ = 'wines'
    id = Column(Integer, primary_key=True)
    name = Column(String(length=254), nullable=False, )
    description = Column(Text, nullable=False)
    image = Column(String(length=500), nullable=True)
    subtitle = Column(String(length=500), nullable=True)
    country = Column(String(length=500), nullable=True)
    region = Column(String(length=500), nullable=True)
    volume = Column(String(length=500), nullable=True)
    vintage = Column(String(length=500), nullable=True)
    wine_type = Column(String(length=500), nullable=True)
    wine_color = Column(String(length=500), nullable=True)
    ingredients = Column(Text, nullable=True)
    sweetness = Column(Integer, nullable=True)
    acidity = Column(Integer, nullable=True)
    tannin = Column(Integer, nullable=True)
    body = Column(Integer, nullable=True)
    bubbles = Column(Integer, nullable=True)
    style = Column(String(length=500), nullable=True)
    aromas_flavors = Column(Text, nullable=True)
    wine_maker = Column(String(length=500), nullable=True)
    dominant_flavors = Column(String(length=500), nullable=True)
    process_in_the_vineyard = Column(String(length=500), nullable=True)
    process_in_the_cellar = Column(String(length=500), nullable=True)
    wine_pairing = Column(String(length=500), nullable=True)
    location = Column(String(length=500), nullable=True)
    vinyard_name = Column(String(length=500), nullable=True)
    altitude = Column(String(length=500), nullable=True)
    yield_in_hector = Column(Float, nullable=True)
    products = relationship("Product", back_populates="wine")
    documents = relationship("WineDocument", back_populates="wine")
    nutritional_info = relationship(
        "WineNutritionalInfo", back_populates="wine", uselist=False,)

    def save_image_to_s3(file: UploadFile) -> str:
        """
        Save the image file to Amazon S3 bucket and return the URL.
        """
        # Generate a unique key for the image
        image_key = f"images/{file.filename}"

        # Upload file to S3
        settings.s3_client.upload_fileobj(file.file, 'hos_app', image_key)

        # Generate the URL for the uploaded image
        image_url = f"https://hos_app.s3.amazonaws.com/{image_key}"

        return image_url


class WineNutritionalInfo(Base):

    __tablename__ = 'wine_nutritional_info'
    id = Column(Integer, primary_key=True)
    wine_id = Column(
        Integer, ForeignKey('wines.id'), unique=True)
    wine = relationship(
        "Wine", back_populates="nutritional_info")
    total_fat = Column(Float, nullable=True, default=0.0)
    saturated_fat = Column(Float, nullable=True, default=0.0)
    trans_fat = Column(Float, nullable=True, default=0.0)
    polyunsaturated_fat = Column(Float, nullable=True, default=0.0)
    monounsaturated_fat = Column(Float, nullable=True, default=0.0)
    cholesterol = Column(Float, nullable=True, default=0.0)
    salt = Column(Float, nullable=True, default=0.0)
    total_carbohydrates = Column(Float, nullable=True, default=0.0)
    dietary_fiber = Column(Float, nullable=True, default=0.0)
    sugars = Column(Float, nullable=True, default=0.0)
    added_sugars = Column(Float, nullable=True, default=0.0)
    sugar_alcohols = Column(Float, nullable=True, default=0.0)
    protein = Column(Float, nullable=True, default=0.0)
    # vitamins
    vitamin_units = Column(String(length=500), nullable=True, default="")
    vitamin_a = Column(Float, nullable=True, default=0.0)
    vitamin_c = Column(Float, nullable=True, default=0.0)
    vitamin_d = Column(Float, nullable=True, default=0.0)
    vitamin_e = Column(Float, nullable=True, default=0.0)
    vitamin_k = Column(Float, nullable=True, default=0.0)
    calcium = Column(Float, nullable=True, default=0.0)
    iron = Column(Float, nullable=True, default=0.0)
    potassium = Column(Float, nullable=True, default=0.0)


class Product(Base):

    __tablename__ = 'products'
    wine_id = Column(Integer, ForeignKey('wines.id'))  # Define foreign key relationship
    wine = relationship("Wine", back_populates="products")
    id = Column(Integer, primary_key=True)
    name = Column(String(length=500), nullable=False)
    percentage = Column(Integer, nullable=False)


class WineDocument(Base):

    __tablename__ = 'wine_documents'
    id = Column(Integer, primary_key=True)
    wine_id = Column(Integer, ForeignKey('wines.id'))  # Define foreign key relationship
    wine = relationship("Wine", back_populates="documents")
    file_url = Column(String(length=500), nullable=False)
    type = Column(Integer, nullable=False)
