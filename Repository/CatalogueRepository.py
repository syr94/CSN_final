
from sqlalchemy import table
#import AbstractRepository
import sys
import os
from sqlalchemy.orm import Session
pwd = os.path.dirname(sys.argv[0])
sys.path.append(pwd + "/../all_classes_list")
#from Driver import Driver
from all_classes_list import *

class CatalogueRepository(AbstractRepository):
    
    table_name = 'catalogue'
    item_obj = Catalogue