import sys
from Repository.SiteCityRepository import SiteCityRepository
from Services.SiteConstructService.SiteConstructAlgorithm import SiteConstructAlgorithm
from Repository.AlgorithmRepository import AlgorithmRepository
from Repository.AlgorithmParameterRepository import AlgorithmParameterRepository
from Repository.AlgorithmParameterValueRepository import AlgorithmParameterValueRepository

class SiteConstractWithXPathParameters(SiteConstructAlgorithm):

    def __init__(self):
        self.site_repository = SiteCityRepository()
        self.algorithm_repository = AlgorithmRepository()
        self.algorithm_parameter_repository = AlgorithmParameterRepository()
        self.algorithm_parameter_value_repository = AlgorithmParameterValueRepository()
        self.algorithm_id = self.algorithm_repository.find_one_by(
            by = "algorithm_class_name", 
            value = self.__class__.__name__
        ).algorithm_id

    def add_site_parameters(self, site, site_city_id = 0):
        try:
            algorithm_parameters = self.algorithm_parameter_repository.get_algorithm_parameters_name_values(
                algorithm_id = self.algorithm_id,
                site_city_id = site_city_id
            )

            for algorithm_parameter_key in algorithm_parameters:
                site.algorithm_parameter_key = algorithm_parameters[algorithm_parameter_key]
        except:
            print("Cannot construct site")
            e = sys.exc_info()[1]
            print(e.args[0])
        