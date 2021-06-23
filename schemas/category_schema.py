from pydantic import BaseModel, constr
from typing import Optional

class Category(BaseModel):
    id: int
    name: constr(min_length=3, max_length=50)
    description: Optional[constr(min_length=1, max_length=300)]
    logo: Optional[constr(min_length=1, max_length=150)]

    class Config:
        orm_mode = True

class InsertCategory(BaseModel):
    name: constr(min_length=3, max_length=50)
    description: Optional[constr(min_length=1, max_length=300)]
    logo: Optional[constr(min_length=1, max_length=150)]

    class Config:
        orm_mode = True

