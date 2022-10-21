from abc import abstractclassmethod, abstractmethod, ABC

class SiteConstructAlgorithm(ABC):

    @abstractmethod
    def add_site_parameters(self)-> str:
        pass
