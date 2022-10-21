from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Algorithm(Base):
    '''
        Model of all algorithm services for different things

    '''
    __tablename__ = 'algorithm'

    algorithm_id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    algorithm_type = Column(String(255))
    algorithm_class_name = Column(String(255))
    algorithm_description = Column(String(255))