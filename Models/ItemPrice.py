from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ItemPrice(Base):
    __tablename__ = 'item_price'

    item_id = Column(Integer, nullable=False, unique=True, primary_key=True)
    price = Column(Float)
    parse_state_id = Column(Integer)

    def __init__(self,
            item_id : int = None,
            price : float = None,
            parse_state_id : int = None) -> None:
        self.item_id = item_id
        self.price = price
        self.parse_state_id = parse_state_id