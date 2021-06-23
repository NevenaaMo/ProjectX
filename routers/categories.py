from models import categories
from database import get_db
from fastapi import APIRouter, status, HTTPException
from typing import List
from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session

from schemas import category_schema
from services import category_service


router = APIRouter(
    prefix="/categories", 
    tags=["categories"])


@router.get("/", response_model=List[category_schema.Category], status_code=status.HTTP_200_OK)
def get_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    categories = category_service.get_all(db, skip, limit)
    if categories is None or len(categories) < 1:
        raise HTTPException(status_code=status.HTTP_200_OK, detail="No categories found!")
    return categories

@router.get("/{category_id}", response_model=category_schema.Category, status_code=status.HTTP_200_OK)
def get_category_by_id(category_id: int, db: Session = Depends(get_db)):
    category = category_service.get_by_id(db, category_id)
    if category is None:
        raise HTTPException(status_code=status.HTTP_200_OK, detail="Category not found")
    return category

@router.post("/", status_code=status.HTTP_201_CREATED, response_description="Successfully added categories")
def insert_categories(category: category_schema.InsertCategory, db: Session = Depends(get_db)):
    if category is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="No categories found.")
    categoriess = category_service.insert_category(db, category)
    return categoriess 

@router.put("/", status_code=status.HTTP_202_ACCEPTED, response_description="Successfully updated categories.")
def edit_categories(categories: List[category_schema.Category], db: Session = Depends(get_db)):
    
    if len(categories) < 1:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="No categories found in the request.")

    categoriess = category_service.edit_categories(db, categories)
    return categoriess