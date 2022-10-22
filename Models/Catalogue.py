from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import PrimaryKeyConstraint
Base = declarative_base()

class Catalogue(Base):
    '''
        Manipulates with Catalogue

    '''
    __tablename__ = 'catalogue'

    #catalogue_id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    #_catalogue_id: int = None
    url = Column(String(255), nullable=False, unique = True, primary_key=True)
    name = Column(String(255), nullable=False, unique = True)
    site_city_id = Column(Integer)
    actual = Column(Integer, nullable=False)

    
    def __init__(self,
            url : str = None,
            name : str = None,   
            site_city_id : int = None,  
            actual : int = None) -> None:
        self.url = url
        self.name = name 
        self.site_city_id = site_city_id
        self.actual = actual