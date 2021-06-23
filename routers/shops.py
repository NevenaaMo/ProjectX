from database import get_db
from fastapi import APIRouter, status, HTTPException
from typing import List
from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session

from schemas import shop_schema
from services import shop_service


router = APIRouter(
    prefix="/shops", 
    tags=["shops"])



#todo GET all /shops/ params limit and skip returns a list of shops 
#todo GET by id /shops/{shop_id} params shop_id returns a shop object
#todo POST insert shop /shops/ params shop object returns 201 created
#todo PUT edit shop /shops/ params shop object, returns updated shop
#todo GET shops by category id /shops/categories/{category_id} params category id returns a list of shops for the given category


@router.get("/", response_model=List[shop_schema.Shop], status_code=status.HTTP_200_OK)
def get_shops(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    shops = shop_service.get_all(db, skip, limit)
    if shops is None or len(shops) < 1:
        raise HTTPException(status_code=status.HTTP_200_OK, detail="No shops found!")
    return shops


@router.get("/{shop_id}", response_model=shop_schema.Shop, status_code=status.HTTP_200_OK)
def get_shop_by_id(shop_id: int, db: Session = Depends(get_db)):
    shop = shop_service.get_by_id(db, shop_id)
    if shop is None:
        raise HTTPException(status_code=status.HTTP_200_OK, detail="Shop not found")
    return shop

@router.post("/", status_code=status.HTTP_201_CREATED, response_description="Successfully added shops")
def insert_shop(shop: shop_schema.InsertShop, db: Session = Depends(get_db)):
    if shop is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="No shops found.")
    shopp = shop_service.insert_shop(db, shop)
    return shopp 

@router.put("/", status_code=status.HTTP_202_ACCEPTED, response_description="Successfully updated shops.")
def edit_shops(shops: List[shop_schema.EditShop], db: Session = Depends(get_db)):
    if len(shops) < 1:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="No shops found in the request.")

    shopp = shop_service.edit_shops(db, shops)
    return shopp

@router.get("/categories/{category_id}", response_model=shop_schema.Shop, status_code=status.HTTP_200_OK)
def get_by_category_id(category_id: int, db: Session=Depends(get_db)):
    shop = shop_service.get_by_category_id(db, category_id)
    if shop is None:
        raise HTTPException(status_code=status.HTTP_200_OK, detail="Shop not found")
    return shop