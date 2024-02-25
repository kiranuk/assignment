from typing import Optional, List, Dict, Union

from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    percentage: int


class ProductOutDBBase(BaseModel):
    id: int
    name: str
    percentage: int

    class Config:
        orm_mode = True


class NutritionalCreate(BaseModel):

    total_fat: Optional[int]
    saturated_fat: Optional[int]
    trans_fat: Optional[int]
    polyunsaturated_fat: Optional[int]
    monounsaturated_fat: Optional[int]
    cholesterol: Optional[int]
    salt: Optional[int]
    total_carbohydrates: Optional[int]
    dietary_fiber: Optional[int]
    sugars: Optional[int]
    added_sugars: Optional[int]
    sugar_alcohols: Optional[int]
    protein: Optional[int]
    vitamin_units: Optional[str]
    vitamin_a: Optional[int]
    vitamin_c: Optional[int]
    vitamin_d: Optional[int]
    vitamin_e: Optional[int]
    vitamin_k: Optional[int]
    calcium: Optional[int]
    iron: Optional[int]
    potassium: Optional[int]

    class Config:
        orm_mode = True


class NutritionalInfo(NutritionalCreate):
    id: int


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
    nutritional_info: NutritionalCreate

    class Config:
        orm_mode = True


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
    products: Optional[List] = []
    nutritional_info: NutritionalInfo

    class Config:
        orm_mode = True


class WineDocumentSchema(BaseModel):
    id: int
    wine_id: int
    document: bytes
    document_type: str

    class Config:
        orm_mode = True