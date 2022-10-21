from Repository.AbstractRepository import AbstractRepository
from Models.AlgorithmParameterValue import AlgorithmParameterValue

class AlgorithmParameterValueRepository(AbstractRepository):
    
    table_name = 'algorithm_parameter_value'
    item_obj = AlgorithmParameterValue