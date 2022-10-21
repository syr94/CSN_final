from abc import abstractclassmethod, abstractmethod, ABC
class CatalogueListParsingAlgorithmService(ABC):

    @abstractmethod
    def get_catalogue_list(self)-> list:
        pass