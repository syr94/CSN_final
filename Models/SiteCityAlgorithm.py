from datetime import date
import sys
from sqlalchemy import Column
from sqlalchemy import Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class SiteCityAlgorithm(Base):
    '''
        describes relation beetween site_id && city_id  and algorithm
    
    '''
    __tablename__ = 'site_city_algorithm'

    site_city_algorithm_id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    site_city_id = Column(Integer)
    algorithm_id = Column(Integer)