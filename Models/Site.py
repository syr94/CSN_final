from datetime import date
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Date
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Site(Base):
    '''
        site Entity
    
    '''
    __tablename__ = 'site'

    site_id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, unique = True)
    main_page_url = Column(String(255), nullable=False, unique = True)
    parse_id = Column(Integer)

    def __init__(self,
            site_id : int = None,
            name : str = None,
            main_page_url : str = None) -> None:
        self.site_id = site_id
        self.name = name
        self.main_page_url = main_page_url

