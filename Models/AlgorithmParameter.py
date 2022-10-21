from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class AlgorithmParameter(Base):
    '''
        Model of all algorithm services for different things

    '''
    __tablename__ = 'algorithm_parameter'

    algorithm_parameter_id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    parameter_name = Column(String(255))
    algorithm_id = Column(Integer)
    necessarily = Column(Integer)