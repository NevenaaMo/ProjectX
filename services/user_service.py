from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models import users
from schemas import user_schema
from helpers.authentication import get_password_hash
from typing import List
from sqlalchemy.exc import SQLAlchemyError


def get_all(db:Session, skip:int = 0, limit:int = 100):
    return db.query(users.User).offset(skip).limit(limit).all()


def get_by_id(db:Session, user_id: int):
    return db.query(users.User).filter(users.User.id == user_id).first()


def get_by_email(db:Session, email:str):
    return db.query(users.User).filter(users.User.email==email).first()


def get_by_country_id(db:Session, country_id: int):
    return db.query(users.User).filter(users.User.country_id == country_id).first()


def get_by_usertiers_id(db:Session, usertier_id: int):
    return db.query(users.User).filter(users.User.user_tier_id == usertier_id).first()


def insert_user(db:Session, user: user_schema.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = users.User(
        username = user.username,
        email = user.email,
        password = hashed_password,
        status = user.status,
        first_name = user.first_name,
        last_name = user.last_name,
        phone = user.phone,
        profile_image = user.profile_image,
        balance = user.balance,
        user_tier_id = user.user_tier_id,
        country_id = user.country_id
    )
    try:
        db.add(db_user)
        db.commit()
        return db_user
    except SQLAlchemyError:
        db.rollback()
        return None
