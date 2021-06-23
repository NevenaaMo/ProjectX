"""A module containing the necessary code for the SQLAlchemy Users model"""
from database import Base
from sqlalchemy import Column, Integer, String, SmallInteger, ForeignKey, BigInteger
from sqlalchemy import DateTime, func
from sqlalchemy.orm import relationship


class Country(Base):
   
    __tablename__ = "countries"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True, index=True)
    code = Column(String(3), nullable=False)


    def __init__(self, name: str, code: str):
        
        self.name = name
        self.code = code


    def __repr__(self):
 
        return """<UserTier(name'{0}', code'{1}'>
            """.format(self.name, self.code)
