from abc import abstractclassmethod
from Services.CatalogueListParsingService.CatalogueListParsingAlgorithmService import CatalogueListParsingAlgorithmService
from Repository.CatalogueRepository import CatalogueRepository
from Models.Catalogue import Catalogue

class Cataloguinator():


    def __init__(
            self,
            catalogue_list_parsing_algorithm : CatalogueListParsingAlgorithmService,
            driver,
            site_city_id
            ) -> None:
        self._catalogue_list_parsing_algorithm = catalogue_list_parsing_algorithm
        self._driver =  driver
        self._site_city_id = site_city_id

    @property
    def catalogue_list_parsing_algorithm(self) -> CatalogueListParsingAlgorithmService:
        return self._catalogue_list_parsing_algorithm

    @catalogue_list_parsing_algorithm.setter
    def catalogue_list_parsing_algorithm(
            self,
            catalogue_list_parsing_algorithm: CatalogueListParsingAlgorithmService
            ) -> None:
        self._catalogue_list_parsing_algorithm = catalogue_list_parsing_algorithm

    def add_catalogue_list_for_site(self,
            site,
            parse_catalogues):
        catalogue_repository = CatalogueRepository()
        
        if parse_catalogues:
            catalogues = self._catalogue_list_parsing_algorithm.get_catalogue_list(
                main_page_url = site.main_page_url,
                site_city_id = self._site_city_id,
                driver = self._driver
            )
            for catalogue in catalogues:
                #TODO make it better, may be get_catalogue_list should return dict {name : url}
                #TODO think about how to handle @actual
                catalogue_item = Catalogue(
                    name = catalogue.split('/')[-1],
                    url = catalogue,
                    site_city_id = self._site_city_id,
                    actual = 1
                )
                catalogue_repository.update(catalogue_item)
        else:
            catalogue_items = catalogue_repository.find_all_by(by = "site_city_id", value = self._site_city_id)
            catalogues = [catalogue_item.url for catalogue_item in catalogue_items]
        site.catalogues = catalogues