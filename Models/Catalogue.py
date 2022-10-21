from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Catalogue(Base):
    '''
        Manipulates with Catalogue

    '''
    __tablename__ = 'catalogue'

    catalogue_id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    #_catalogue_id: int = None
    name = Column(String(255), nullable=False, unique = True)
    url = Column(String(255), nullable=False, unique = True)
    site_city_id = Column(Integer)
    actual = Column(Integer, nullable=False)

    def __init__(self,
            catalogue_id : int = None,
            name : str = None,   
            url : str = None,
            site_city_id : int = None,  
            actual : int = None) -> None:
        self.catalogue_id = catalogue_id
        self.name = name 
        self.url = url
        self.site_city_id = site_city_id
        self.actual = actual