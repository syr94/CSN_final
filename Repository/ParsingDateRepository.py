from Repository.AbstractRepository import AbstractRepository
from Models.ParsingDate import ParsingDate

class ParsingDateRepository(AbstractRepository):

    table_name = 'parsing_date'
    item_obj = ParsingDate