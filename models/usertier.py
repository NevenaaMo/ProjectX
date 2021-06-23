"""A module containing the necessary code for the SQLAlchemy Users model"""
from sqlalchemy.sql.sqltypes import Float
from database import Base
from sqlalchemy import Column, Integer, String, SmallInteger, ForeignKey, BigInteger
from sqlalchemy import DateTime, func
from sqlalchemy.orm import relationship


class UserTier(Base):
   
    __tablename__ = "usertiers"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True, index=True)
    min_points = Column(Integer, nullable=False)
    max_points = Column(Integer, nullable=False)
    cashback_multiplier = Column(Float, nullable=False)
    reward_time = Column(Float, nullable=False)


    def __init__(self, name: str, min_points: int, max_points: int, cashback_multiplier: float, reward_time: float):
        
        self.name = name
        self.min_points = min_points
        self.max_points = max_points
        self.cashback_multiplier = cashback_multiplier
        self.reward_time = reward_time

    def __repr__(self):
 
        return """<UserTier(name'{0}', min_points'{1}', max_points'{2}', cashback_multiplier'{3}',
            reward_time'{4}'>
            """.format(self.name, self.min_points,
                       self.max_points, self.cashback_multiplier, self.reward_time)
