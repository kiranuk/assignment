from datetime import datetime

from pydantic import HttpUrl
from sqlalchemy import Column, Integer, Text, String, Boolean, DateTime, ForeignKey, Float, LargeBinary
from sqlalchemy.orm import relationship

from db.base_class import Base


class Wine(Base):

    __tablename__ = 'wines'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    image = Column(LargeBinary, nullable=True)
    subtitle = Column(String, nullable=True)
    country = Column(String, nullable=True)
    region = Column(String, nullable=True)
    volume = Column(String, nullable=True)
    vintage = Column(String, nullable=True)
    wine_type = Column(String, nullable=True)
    wine_color = Column(String, nullable=True)
    ingredients = Column(String, nullable=True)
    nutritional_info = Column(String, nullable=True)
    sweetness = Column(Integer, nullable=True)
    acidity = Column(Integer, nullable=True)
    tannin = Column(Integer, nullable=True)
    body = Column(Integer, nullable=True)
    bubbles = Column(Integer, nullable=True)
    style = Column(String, nullable=True)
    aromas_flavors = Column(String, nullable=True)
    wine_maker = Column(String, nullable=True)
    dominant_flavors = Column(String, nullable=True)
    process_in_the_vineyard = Column(String, nullable=True)
    process_in_the_cellar = Column(String, nullable=True)
    wine_pairing = Column(String, nullable=True)
    location = Column(String, nullable=True)
    vinyard_name = Column(String, nullable=True)
    altitude = Column(String, nullable=True)
    yield_in_hector = Column(Float, nullable=True)
    products = relationship("Product", back_populates="wine")
    documents = relationship("WineDocument", back_populates="wine")


class Product(Base):

    __tablename__ = 'products'
    wine_id = Column(Integer, ForeignKey('wines.id'))  # Define foreign key relationship
    wine = relationship("Wine", back_populates="products")
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    percentage = Column(Integer, nullable=False)


class WineDocument(Base):
    __tablename__ = 'wine_documents'
    id = Column(Integer, primary_key=True)
    wine_id = Column(Integer, ForeignKey('wines.id'))  # Define foreign key relationship
    wine = relationship("Wine", back_populates="documents")
    file_path = Column(String, nullable=False)
    type = Column(Integer, nullable=False)
