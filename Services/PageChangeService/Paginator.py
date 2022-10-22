from abc import abstractclassmethod
from Services.PageChangeService.PageChangeAlgorithmService import PageChangeAlgorithmService
from Driver.Driver import Driver


class Paginator():


    def __init__(self,
            page_change_algorithm : PageChangeAlgorithmService,
            driver = Driver.get_instance(),
            ):
        self._page_change_algorithm = page_change_algorithm
        self._driver = driver
        self._current_catalogue = ''
        
    @property
    def current_catalogue(self) -> str:
        return self._current_catalogue

    @current_catalogue.setter
    def current_catalogue(self, new_current_catalogue) -> None:
        self._current_catalogue = new_current_catalogue


    def get_next_page(self):
        pagination_link = self._page_change_algorithm.get_next_page(self._current_catalogue)
        return pagination_link