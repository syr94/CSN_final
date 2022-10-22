from abc import abstractclassmethod
from Services.SiteItemArticulGetService.ArticulGetAlgorithm import ArticulGetAlgorithm
from Driver.Driver import Driver


class Articulinator():


    def __init__(self,
            articul_get_algorithm : ArticulGetAlgorithm,
            driver = Driver.get_instance(),
            ):
        self._articul_get_algorithm = articul_get_algorithm
        self._driver = driver
        

    def get_articul(self, block):
        articul = self._articul_get_algorithm.get_articul_from_block(block)
        return articul

    def get_url(self, block):
        item_url = self._articul_get_algorithm.get_item_url(block)
        return item_url