from os import name
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models import categories
from schemas import category_schema
from typing import List
from sqlalchemy.exc import SQLAlchemyError


def get_all(db:Session, skip:int = 0, limit:int = 100):
    return db.query(categories.Category).offset(skip).limit(limit).all()


def get_by_id(db:Session, category_id: int):
    return db.query(categories.Category).filter(categories.Category.id == category_id).first()


def insert_category(db: Session, category: category_schema.InsertCategory):
    db_category = categories.Category(
        name=category.name,
        description=category.description,
        logo=category.logo,
    )
    try:
        db.add(db_category)
        db.commit()
        return True
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail="Problem while inserting categories! or" + str(type(e)))


def edit_categories(db: Session, categories: List[category_schema.Category]):
    db_categories = []
    for category in categories:
        db_category = get_by_id(db, category.id)
        update_data = category.dict(exclude_unset=True)
        for key, value in update_data.items():
            if(value != db_category.id):
                setattr(db_category, key, value)
        db_categories.append(db_category)
    try:
        db.bulk_save_objects(db_categories)
        db.commit()
        return True
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Problem while updating categories! or " + str(type(e)))