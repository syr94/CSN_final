from Repository.AbstractRepository import AbstractRepository
import sys
from Models.SiteCity import SiteCity
from sqlalchemy.orm import Session

class SiteCityRepository(AbstractRepository):

    table_name = 'site_city'
    item_obj = SiteCity

    def get_site_city(self, site_id = 0, city_id = 0) -> list:
        with Session(self.engine) as session:
            try:
                return session.query(SiteCity).filter(
                    SiteCity.site_id.like(site_id),
                    SiteCity.city_id.like(city_id)
                ).first().site_city_id
            except:
                e = sys.exc_info()[1]
                print(e.args[0])