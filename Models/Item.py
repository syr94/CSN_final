from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import VARCHAR, Column, ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
#from mysql.connector import connect, Error
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import sys

Base = declarative_base()

class Item(Base):
    '''
        Describes Item
        
    '''
    __tablename__ = 'item'

    id = Column(Integer, nullable=False, unique = True, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(255), nullable=False, unique = True)
    url  = Column(VARCHAR(255), unique = True)
    inner_site_id = Column(VARCHAR(255), unique = True)
 
    def __init__(self, name : str = '', url : str = '', inner_site_id : str = '') -> None:
        self.name = name
        self.url = url
        self.inner_site_id = inner_site_id