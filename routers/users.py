from database import get_db
from fastapi import APIRouter, status, HTTPException
from typing import List
from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session

from schemas import user_schema
from services import user_service


router = APIRouter(
    prefix="/users", 
    tags=["users"])


@router.get("/", response_model=List[user_schema.User], status_code=status.HTTP_200_OK)
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = user_service.get_all(db, skip, limit)
    if users is None or len(users) < 1:
        raise HTTPException(status_code=status.HTTP_200_OK, detail="No users found!")
    return users


@router.get("/{user_id}", response_model=user_schema.User, status_code=status.HTTP_200_OK)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = user_service.get_by_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_200_OK, detail="User not found")
    return user


@router.get("/countries/{country_id}", response_model=user_schema.User, status_code=status.HTTP_200_OK)
def get_user_by_country_id(country_id: int, db: Session = Depends(get_db)):
    user = user_service.get_by_country_id(db, country_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_200_OK, detail="User not found")
    return user


@router.get("/tiers/{tier_id}", response_model=user_schema.User, status_code=status.HTTP_200_OK)
def get_user_by_usertiers_id(tier_id: int, db: Session = Depends(get_db)):
    user = user_service.get_by_usertiers_id(db, tier_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_200_OK, detail="User not found")
    return user
