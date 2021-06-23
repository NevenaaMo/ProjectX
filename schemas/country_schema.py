from pydantic import BaseModel, constr
from typing import Optional

class Country(BaseModel):
    id: int
    name: constr(min_length=3, max_length=100)
    code: constr(min_length=1, max_length=3)

    class Config:
        orm_mode = True


class CountryEdit(BaseModel):
    id: int
    name: Optional[constr(min_length=3, max_length=100)]
    code: Optional[constr(min_length=1, max_length=3)]

    class Config:
        orm_mode = True