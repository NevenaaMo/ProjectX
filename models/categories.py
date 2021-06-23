"""A module containing the necessary code for the SQLAlchemy Users model"""
from os import name
from database import Base
from sqlalchemy import Column, Integer, String, SmallInteger, ForeignKey, BigInteger
from sqlalchemy import DateTime, func
from sqlalchemy.orm import relationship


class Category(Base):
   
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(300))
    logo = Column(String(150))


    def __init__(self, name:str, description: str, logo: str):
        self.name = name 
        self.description = description
        self.logo = logo


    def __repr__(self):
 
        return """<Category(name'{0}', description'{1}', logo'{2}'>
            """.format(self.name, self.description, self.logo)
