from os import name
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models import shops, categories
from schemas import shop_schema
from typing import List
from sqlalchemy.exc import SQLAlchemyError


def get_all(db:Session, skip:int = 0, limit:int = 100):
    return db.query(shops.Shop).offset(skip).limit(limit).all()


def get_by_id(db:Session, shop_id: int):
    return db.query(shops.Shop).filter(shops.Shop.id == shop_id).first()


def get_by_category_id(db:Session, categoryid: int):
    return db.query(shops.Shop).filter(shops.Shop.category_id == categoryid).first()


def insert_shop(db: Session, shop: shop_schema.InsertShop):
    db_shop = shops.Shop(
        name=shop.name,
        description=shop.description,
        cashback_percentage=shop.cashback_percentage,
        logo=shop.logo,
        category_id=shop.category_id
    )
    try:
        db.add(db_shop)
        db.commit()
        return True
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail="Problem while inserting shop! or" + str(type(e)))


def edit_shops(db: Session, shops: List[shop_schema.EditShop]):
    db_shops = []
    for shop in shops:
        db_shop = get_by_id(db, shop.id)
        update_data = shop.dict(exclude_unset=True)
        for key, value in update_data.items():
            if(value != db_shop.id):
                setattr(db_shop, key, value)
        db_shops.append(db_shop)
    try:
        db.bulk_save_objects(db_shops)
        db.commit()
        return True
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Problem while updating shops! or " + str(type(e)))