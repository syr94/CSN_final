from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()

class ItemParameter(Base):
    __tablename__ = 'item_parameter'

    parameter_id = Column(Integer, primary_key=True, autoincrement=True)
    parameter_name = Column(String(255))
    parameter_description = Column(String(255))

    def __init__(self,
            parameter_id : int = None,
            parameter_name : str = None,
            parameter_description : str = '') -> None:
        self.parameter_id = parameter_id
        self.parameter_name = parameter_name
        self.parameter_description = parameter_description