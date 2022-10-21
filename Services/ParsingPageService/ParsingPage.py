from abc import abstractclassmethod
from Services.ParsingPageService.ParsingPageAlgorithmService import ParsingPageAlgorithmService


class ParsingPage():


    def __init__(self,
            page_change_algorithm : ParsingPageAlgorithmService,
            paginator_options : dict = {}) -> None:
        self._page_change_algorithm = page_change_algorithm
        self._paginator_options = paginator_options

    @property
    def parsing_page_algorithm(self) -> ParsingPageAlgorithmService:

        return self._parsing_page_algorithm

    @parsing_page_algorithm.setter
    def parsing_page_algorithm(self,
            parsing_page_algorithm: parsing_page_algorithm,
            paginator_options : dict = {}) -> None:
        self._parsing_page_algorithm = parsing_page_algorithm

    @abstractclassmethod
    def parse_page(self):
        pass