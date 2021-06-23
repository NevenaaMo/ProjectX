from pydantic import BaseModel, constr
from typing import Optional

class UserTier(BaseModel):
    id: int
    name: constr(min_length=3, max_length=50)
    min_points: int
    max_points: int
    cashback_multiplier: float
    reward_time: float

    class Config:
        orm_mode = True