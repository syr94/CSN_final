from Repository.AbstractRepository import AbstractRepository
from Models.Algorithm import Algorithm
from sqlalchemy.orm import Session
from sqlalchemy import text
import sys

class AlgorithmRepository(AbstractRepository):
    
    table_name = 'algorithm'
    item_obj = Algorithm

    def get_algorithms_for_site(self, site_city_id : int) -> dict:
        with Session(self.engine) as session:
            try:
                algorithms = {}
                #TODO this query better than python thing site_city
                '''
                select * from site_city where site_city_id in(
                select ifnull(sc3.site_city_id, sc.site_city_id)from site_city sc 
                left join site_city as sc3 on sc3.site_id=sc.site_id and sc3.city_id = 5
                where sc.site_id = 1 and sc.city_id =0)
                '''
                # without shlyapa with site_id = site_id it looks not good
                query = text("SELECT algorithm_type, algorithm_class_name  from `algorithm` a "\
                                "LEFT JOIN site_city_algorithm sca ON a.algorithm_id = sca.algorithm_id "\
	                                "WHERE site_city_id = {site_city_id}"\
                            .format(site_city_id = site_city_id)) 

                algorithms_list = [algorithms.update({
                                        algorithm.algorithm_type : algorithm.algorithm_class_name
                                    }) 
                                    for algorithm in  session.execute(query).all()
                                    ]
                
                return algorithms

            except Exception:
                e = sys.exc_info()[1]
                print(e.args[0])

