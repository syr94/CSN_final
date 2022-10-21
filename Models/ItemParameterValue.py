from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class ItemParameterValue(Base):
    '''
        Describes parameters of Item

    '''
    __tablename__ = 'item_parameter_value'

    item_parameter_value_id = Column(Integer, primary_key=True)
    item_id = Column(Integer, nullable=False)
    parameter_id = Column(Integer, nullable=False)
    value = Column(String)

    def __init__(self,
            item_id : int = None,
            parameter_id : int = None,
            value : str = '') -> None:
        self.parameter_id = parameter_id
        self.item_id = item_id
        self.value = value