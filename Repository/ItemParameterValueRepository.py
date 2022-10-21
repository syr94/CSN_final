from Repository.AbstractRepository import AbstractRepository
from Models.ItemParameterValue import ItemParameterValue

class ItemParameterValueRepository(AbstractRepository):

    table_name = 'item_parameter_value'
    item_obj = ItemParameterValue