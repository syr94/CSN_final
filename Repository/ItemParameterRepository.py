from Repository.AbstractRepository import AbstractRepository
from Models.ItemParameter import ItemParameter

class ItemParameterRepository(AbstractRepository):

    table_name = 'item_parameter'
    item_obj = ItemParameter