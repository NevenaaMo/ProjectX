from pydantic import BaseModel as PydanticBaseModel
from pydantic import constr, EmailStr
from typing import Optional
from schemas.country_schema import Country
from schemas.usertier_schema import UserTier

class BaseModel(PydanticBaseModel):
    class Config:
        arbitraty_types_allowed = True

class User(BaseModel):
    id: int
    username: constr(min_length=3, max_length=20)
    email: EmailStr
    status: int
    first_name: constr(min_length=1, max_length=50)
    last_name: constr(min_length=1, max_length=50)
    phone: Optional[constr(regex='^\+(?:[0-9] ?){6,14}[0-9]$')]
    profile_image: Optional[constr(min_length=1, max_length=150)]
    balance: int
    user_tier_id: int
    usertier: UserTier
    country_id: int
    country: Country

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    username: constr(min_length=3, max_length=20)
    email: EmailStr
    password: constr(
        regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$")
    confirm_password: constr(
        regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$")
    status: int = 1
    first_name: constr(min_length=1, max_length=50)
    last_name: constr(min_length=1, max_length=50)
    phone: Optional[constr(regex='^\+(?:[0-9] ?){6,14}[0-9]$')]
    profile_image: Optional[constr(min_length=1, max_length=150)] 
    balance: Optional[int] = 0
    user_tier_id: int
    country_id: int

    class Config:
        orm_mode = True