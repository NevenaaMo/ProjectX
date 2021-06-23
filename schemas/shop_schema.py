from pydantic import BaseModel, constr
from typing import Optional
from schemas.category_schema import Category

class Shop(BaseModel):
    id: int
    name: constr(min_length=3, max_length=100)
    description: Optional[constr(min_length=3, max_length=300)]
    cashback_percentage: float
    logo: Optional[constr(min_length=1, max_length=150)]
    category_id: int
    category: Category

    class Config:
        orm_mode = True

class InsertShop(BaseModel):
    name: constr(min_length=3, max_length=100)
    description: Optional[constr(min_length=3, max_length=300)]
    cashback_percentage: float
    logo: Optional[constr(min_length=1, max_length=150)]
    category_id: int

    class Config:
        orm_mode = True

class EditShop(BaseModel):
    id: int
    name: Optional[constr(min_length=3, max_length=100)]
    description: Optional[constr(min_length=3, max_length=300)]
    cashback_percentage: Optional[float]
    logo: Optional[constr(min_length=1, max_length=150)]
    category_id: Optional[int]

    class Config:
        orm_mode = True