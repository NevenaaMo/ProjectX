from database import get_db
from fastapi import APIRouter, status, HTTPException
from typing import List
from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session

from schemas import country_schema
from services import country_service


router = APIRouter(
    prefix="/countries", 
    tags=["countries"])


@router.get("/", response_model=List[country_schema.Country], status_code=status.HTTP_200_OK)
def get_countries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    countries = country_service.get_all(db, skip, limit)
    if countries is None or len(countries) < 1:
        raise HTTPException(status_code=status.HTTP_200_OK, detail="No countries found!")
    return countries

@router.get("/{country_id}", response_model=country_schema.Country, status_code=status.HTTP_200_OK)
def get_country_by_id(country_id: int, db: Session = Depends(get_db)):
    country = country_service.get_by_id(db, country_id)
    if country is None:
        raise HTTPException(status_code=status.HTTP_200_OK, detail="Country not found")
    return country


@router.put("/", status_code=status.HTTP_202_ACCEPTED, response_description="Successfully updated countries.")
def edit_countries(countries: List[country_schema.CountryEdit], db: Session = Depends(get_db)):
    
    if len(countries) < 1:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="No countries found in the request.")

    countries = country_service.edit_countries(db, countries)
    return countries