from sqlalchemy import Date
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class ParsingDate(Base):
    '''
        Describes start and end parsing of Item
    '''
    __tablename__ = 'parsing_date'

    parsing_id = Column(Integer, primary_key =True)
    parsing_start_date = Column(Date)
    parsing_end_date = Column(Date)