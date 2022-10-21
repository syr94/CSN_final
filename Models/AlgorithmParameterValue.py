from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class AlgorithmParameterValue(Base):
    '''
        Model of all algorithm services for different things

    '''
    __tablename__ = 'algorithm_parameter_value'

    algorithm_parameter_value_id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    site_city_id = Column(Integer)
    algorithm_parameter_id = Column(Integer)
    parameter_value = Column(String(255))