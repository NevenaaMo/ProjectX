"""A module containing the necessary code for the SQLAlchemy Users model"""
from database import Base
from sqlalchemy import Column, Integer, String, SmallInteger, ForeignKey, BigInteger
from sqlalchemy import DateTime, func
from sqlalchemy.orm import relationship
from models.countries import Country
from models.usertier import UserTier


class User(Base):
  
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False, unique=True, index=True)
    email = Column(String(50), nullable=False, unique=True, index=True)
    password = Column(String(100), nullable=False)
    status = Column(SmallInteger, nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    phone = Column(String(30), nullable=True)
    profile_image = Column(String(150), nullable=True)
    balance = Column(BigInteger, nullable=False)
    user_tier_id = Column(Integer, ForeignKey('usertier.id'), nullable=False)
    usertier = relationship("UserTier", backref="users")
    country_id = Column(Integer, ForeignKey('countries.id'), nullable=False)
    country = relationship("Country", backref="users")

    def __init__(self, username: str, email: str, password: str, status: int, first_name: str, last_name: str, phone: str, profile_image: str, balance: int, user_tier_id: int, country_id: int):
        
        self.username = username
        self.email = email
        self.password = password
        self.status = status
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.profile_image = profile_image
        self.balance = balance
        self.user_tier_id = user_tier_id
        self.country_id = country_id

    def __repr__(self):
  
        return """<User(username'{0}', email'{1}', password'{2}', status'{3}',
            first_name'{4}', last_name'{5}', phone'{6}', profile_image'{7}', 
            balance'{8}', user_tier_id'{9}', country_id'{10}'>
            """.format(self.username, self.email,
                       self.password, self.status, self.first_name, self.last_name, self.phone,
                       self.profile_image, self.balance, self.user_tier_id, self.country_id)
