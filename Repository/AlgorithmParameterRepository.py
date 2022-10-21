from Repository.AbstractRepository import AbstractRepository
from Models.AlgorithmParameter import AlgorithmParameter
from sqlalchemy.orm import Session
from sqlalchemy import text
import sys

class AlgorithmParameterRepository(AbstractRepository):
    
    table_name = 'algorithm_parameter'
    item_obj = AlgorithmParameter

    def get_algorithm_parameters_name_values(self, algorithm_id : int, site_city_id : int) -> dict:
        with Session(self.engine) as session:
            try:
                site_parameters = {}
                # without shlyapa with site_id = site_id it looks not good
                query = text("SELECT ap.parameter_name, apv.parameter_value FROM `algorithm_parameter` ap "\
                                "LEFT JOIN `algorithm_parameter_value` apv ON "\
                                    "ap.algorithm_parameter_id = apv.algorithm_parameter_id "       
	                                "WHERE algorithm_id = {algorithm_id} and site_city_id = {site_city_id}"\
                            .format(algorithm_id = algorithm_id, site_city_id = site_city_id)) 

                [site_parameters.update({
                    algorithm_parameter.parameter_name : algorithm_parameter.parameter_value
                })
                        for algorithm_parameter 
                        in session.execute(query).all()
                ]
                
                return dict(site_parameters)
            
            except Exception:
                e = sys.exc_info()[1]
                print(e.args[0])