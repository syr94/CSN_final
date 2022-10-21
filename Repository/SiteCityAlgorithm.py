from Repository.AbstractRepository import AbstractRepository
import sys
from Models.SiteCityAlgorithm import SiteCityAlgorithm

class SiteCityRepository(AbstractRepository):

    table_name = 'site_city_algorithm'
    item_obj = SiteCityAlgorithm
