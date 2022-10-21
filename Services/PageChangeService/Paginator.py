from abc import abstractclassmethod
from Services.PageChangeService.PageChangeAlgorithmService import PageChangeAlgorithmService


class Paginator():


    def __init__(self,
            page_change_algorithm : PageChangeAlgorithmService,
            paginator_options : dict = {}) -> None:
        self._page_change_algorithm = page_change_algorithm
        self._paginator_options = paginator_options

    @property
    def page_change_algorithm(self) -> PageChangeAlgorithmService:

        return self._page_change_algorithm

    @page_change_algorithm.setter
    def page_change_algorithm(self,
            page_change_algorithm: page_change_algorithm,
            paginator_options : dict = {}) -> None:
        self._page_change_algorithm = page_change_algorithm

    @abstractclassmethod
    def get_next_page(self):
        pass