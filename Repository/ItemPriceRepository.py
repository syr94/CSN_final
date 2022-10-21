from Repository.AbstractRepository import AbstractRepository

import sys
import os
from sqlalchemy.orm import Session
pwd = os.path.dirname(sys.argv[0])
print(pwd)
sys.path.append("/home/web-dev/projects/selenium-parser/")
#from Driver import Driver
from Models.ItemPrice import ItemPrice


class ItemPriceRepository(AbstractRepository):

    table_name = 'item_price'
    item_obj = ItemPrice

