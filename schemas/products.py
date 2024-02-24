from typing import Optional

from pydantic import BaseModel,EmailStr, Field


class ProductCreate(BaseModel):
    name: str
    description: str


class ProductUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]


class ProductOutDBBase(ProductCreate):
    id: int
    created_at: str
    updated_at: str

    class Config:
        orm_mode = True