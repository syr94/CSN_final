from Repository.AbstractRepository import AbstractRepository
from Models.Site import Site

class SiteRepository(AbstractRepository):

    table_name = 'site'
    item_obj = Site