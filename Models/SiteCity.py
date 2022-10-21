from datetime import date
import sys
from sqlalchemy import Column
from sqlalchemy import Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class SiteCity(Base):
    '''
        site Entity
    
    '''
    __tablename__ = 'site_city'

    site_city_id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    city_id = Column(Integer)
    site_id = Column(Integer)