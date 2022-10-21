from datetime import date
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Date
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class City(Base):

    __tablename__ = 'city' 
    city_id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    name = Column(String(50))
    region = Column(Integer)