from abc import abstractclassmethod
from Services.SiteConstructService.SiteConstructAlgorithm import SiteConstructAlgorithm
from Repository.SiteRepository import SiteRepository
from Repository.SiteCityRepository import SiteCityRepository


class SiteConstructService():


    def __init__(self,
            site_construct_algorithm : SiteConstructAlgorithm,
            site_id : int) -> None:
        self._site_repository = SiteRepository()
        self._site_city_repository = SiteCityRepository()
        self._site_construct_algorithm = site_construct_algorithm
        self._site_id = site_id

    @property
    def site_construct_algorithm(self) -> SiteConstructAlgorithm:

        return self._site_construct_algorithm

    @site_construct_algorithm.setter
    def site_construct_algorithm(self,
            site_construct_algorithm) -> None:
        self._site_construct_algorithm = site_construct_algorithm

    def site_construct(self, site_city_id : int):
        site = self._site_repository.find_one_by(by = "site_id", value = self._site_id)
        self.site_construct_algorithm.add_site_parameters(
            site, 
            site_city_id = site_city_id
        )
        return site