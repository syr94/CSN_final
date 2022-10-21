from abc import abstractclassmethod, abstractmethod, ABC

class ParsingPageAlgorithmService(ABC):
    @abstractmethod
    def parse_page(self)-> list:
        pass