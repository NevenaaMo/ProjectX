from os import access
from database import get_db
from fastapi import APIRouter, status, HTTPException
from typing import List
from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import timedelta

from schemas import user_schema, token_schema
from services import user_service
from helpers import authentication
from helpers.authentication import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token



router = APIRouter(
    tags=["authentication"])


@router.post("/login", response_model=token_schema.Token, status_code=status.HTTP_200_OK)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = user_service.get_by_email(db, form_data.username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/register", response_model=token_schema.Token, status_code=status.HTTP_200_OK)
def register(user: user_schema.UserCreate, db: Session=Depends(get_db)):
    new_user = user_service.insert_user(db, user)
    return new_user