"""A module containing the necessary code for the SQLAlchemy Shops model"""
from sqlalchemy.sql.sqltypes import Float
from database import Base
from sqlalchemy import Column, Integer, String, SmallInteger, ForeignKey, BigInteger
from sqlalchemy import DateTime, func
from sqlalchemy.orm import relationship
from models.categories import Category


class Shop(Base):
  
    __tablename__ = "shops"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True, index=True)
    description = Column(String(300))
    cashback_percentage = Column(Float, nullable=False)
    logo = Column(String(150), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    category = relationship("Category", backref="shops")

    def __init__(self, name: str, description: str, cashback_percentage: float, logo: str, category_id: int):
        
        self.name = name
        self.description = description
        self.cashback_percentage = cashback_percentage
        self.logo = logo
        self.category_id = category_id

    def __repr__(self):
  
        return """<User(name'{0}', description'{1}', cashback_percentage'{2}', logo'{3}',
            category_id'{4}'>
            """.format(self.name, self.description,
                       self.cashback_percentage, self.logo, self.category_id)
