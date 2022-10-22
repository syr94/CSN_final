from abc import abstractclassmethod
from Services.ParsingPageService.ParsingPageAlgorithmService import ParsingPageAlgorithmService
from Driver.Driver import Driver

class ParsingPage():


    def __init__(self,
            parsing_page_algorithm : ParsingPageAlgorithmService,
            driver : Driver = Driver.get_instance()) -> None:
        self._parsing_page_algorithm = parsing_page_algorithm

    @property
    def parsing_page_algorithm(self) -> ParsingPageAlgorithmService:

        return self._parsing_page_algorithm

    @parsing_page_algorithm.setter
    def parsing_page_algorithm(self,
            parsing_page_algorithm: parsing_page_algorithm,
            paginator_options : dict = {}) -> None:
        self._parsing_page_algorithm = parsing_page_algorithm

    
    def parse_page_save_items(self, catalogue : str):
        self._parsing_page_algorithm.parse_page(catalogue)