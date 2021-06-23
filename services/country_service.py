from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models import countries
from schemas import country_schema
from typing import List
from sqlalchemy.exc import SQLAlchemyError

def get_all(db:Session, skip:int = 0, limit:int = 100):
    return db.query(countries.Country).offset(skip).limit(limit).all()

def get_by_id(db:Session, country_id: int):
    return db.query(countries.Country).filter(countries.Country.id == country_id).first()

def edit_countries(db: Session, countries: List[country_schema.CountryEdit]):
    db_countries = []
    for country in countries:
        db_country = get_by_id(db, country.id)
        update_data = country.dict(exclude_unset=True)
        for key, value in update_data.items():
            if(value != db_country.id):
                setattr(db_country, key, value)
        db_countries.append(db_country)
    try:
        db.bulk_save_objects(db_countries)
        db.commit()
        return True
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Problem while updating countries! or " + str(type(e)))