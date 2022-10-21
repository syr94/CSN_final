from abc import abstractclassmethod, abstractmethod, ABC

class PageChangeAlgorithmService(ABC):

    @abstractmethod
    def get_next_page(self)-> str:
        pass
