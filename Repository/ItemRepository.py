from Repository.AbstractRepository import AbstractRepository
from Models.Item import Item

class ItemRepository(AbstractRepository):

    table_name = 'item'
    item_obj = Item
    