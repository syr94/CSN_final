from Repository.AbstractRepository import AbstractRepository
import sys
from Models.City import City

class CityRepository(AbstractRepository):

    table_name = 'city'
    item_obj = City