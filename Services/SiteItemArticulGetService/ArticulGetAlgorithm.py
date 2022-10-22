from abc import abstractclassmethod, abstractmethod, ABC

class ArticulGetAlgorithm(ABC):

    @abstractmethod
    def get_articul_from_block(self)-> str:
        pass

    @abstractmethod
    def get_item_url(self)-> str:
        pass