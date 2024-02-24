from typing import Optional, List

from pydantic import BaseModel,EmailStr, Field


class ProductCreate(BaseModel):
    name: str
    percentage: int


class ProductOutDBBase(BaseModel):
    id: int
    name: str
    percentage: int

    class Config:
        orm_mode = True


class WineCreate(BaseModel):
    name: str
    description: str
    image: Optional[bytes]
    subtitle: Optional[str]
    country: Optional[str]
    region: Optional[str]
    volume: Optional[str]
    vintage: Optional[str]
    wine_type: Optional[str]
    wine_color: Optional[str]
    ingredients: Optional[str]
    nutritional_info: Optional[str]
    sweetness: Optional[int]
    acidity: Optional[int]
    tannin: Optional[int]
    body: Optional[int]
    bubbles: Optional[int]
    style: Optional[str]
    aromas_flavors: Optional[str]
    wine_maker: Optional[str]
    dominant_flavors: Optional[str]
    process_in_the_vineyard: Optional[str]
    process_in_the_cellar: Optional[str]
    wine_pairing: Optional[str]
    location: Optional[str]
    vinyard_name: Optional[str]
    altitude: Optional[str]
    yield_in_hector: Optional[float]
    product: List[ProductCreate]


class WineUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]


class WineOutDBBase(BaseModel):
    id: int
    name: str
    description: str
    image: Optional[bytes]
    subtitle: Optional[str]
    country: Optional[str]
    region: Optional[str]
    volume: Optional[str]
    vintage: Optional[str]
    wine_type: Optional[str]
    wine_color: Optional[str]
    ingredients: Optional[str]
    nutritional_info: Optional[str]
    sweetness: Optional[int]
    acidity: Optional[int]
    tannin: Optional[int]
    body: Optional[int]
    bubbles: Optional[int]
    style: Optional[str]
    aromas_flavors: Optional[str]
    wine_maker: Optional[str]
    dominant_flavors: Optional[str]
    process_in_the_vineyard: Optional[str]
    process_in_the_cellar: Optional[str]
    wine_pairing: Optional[str]
    location: Optional[str]
    vinyard_name: Optional[str]
    altitude: Optional[str]
    yield_in_hector: Optional[float]
    products: List[ProductOutDBBase] = []

    class Config:
        orm_mode = True