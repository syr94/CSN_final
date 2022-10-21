from all_classes_list import *
import os
import logging
from dotenv import load_dotenv
load_dotenv()
import sys


if __name__ == '__main__':

    #Initializing
    try: 
        # TODO: Think about how to take values. argv?
        db_connection_string = os.getenv('DB_CONNECTION_STRING')
        site_id = 1
        city_id = 3

        # Initializing web Driver
        driver = Driver.get_instance()

        #Creating variable wich contains site_city_id, it will be it's own identeficator
        #City 0 - default city
        site_city_repository = SiteCityRepository()
        site_city_id = site_city_repository.get_site_city(site_id = site_id, city_id = city_id)
        if site_city_id is None:
            site_city_id = site_city_repository.get_site_city(site_id = site_id, city_id = 0)

        #Initializing Algorithms for site
        algorithm_repository =  AlgorithmRepository()
        algorithms = algorithm_repository.get_algorithms_for_site(site_city_id = site_city_id)
        
        #   Initializing site parameters to construct service by it's id and city id
        site_construct_service = SiteConstructService(
            site_construct_algorithm = globals()[algorithms['SiteConstruct']](),
            site_id = site_id
        )

        #   Constructing site by it's Algorithm
        site = site_construct_service.site_construct(site_city_id = site_city_id)

        # Creating Cataloguinator for site
        cataloguinator = Cataloguinator(
            catalogue_list_parsing_algorithm = globals()[algorithms['Cataloguinator']](),
            driver = driver,
            site_city_id = site_city_id
        )

        # Getting Catalogues for site
        cataloguinator.add_catalogue_list_for_site(
            site
        )


    except:
        e = sys.exc_info()[1]
        print(e.args[0])

'''
if __name__ == '__main__':
    try:
        with connect(
            **mysql_db
            ) as connection:
            print(connection)
    except Error as e:
        print(e)

    try:
        driver = Driver.get_instance()
        site = sites['set-tehniki']
        cataloguinator = Cataloguinator(FinalWordCategoryAlgorithm(
            site['main_page_url'],
            site['catalogue_element_xpath'],
            site['catalogue_list_item_xpath'],
            driver
        ))

        catalogues = cataloguinator.catalogue_list_parsing_algorithm.get_catalogue_list()
        items = []
        for catalogue in catalogues:
            paginator = Paginator(UrlPageChangeAlgorithm(
                catalogue,
                "?page=",
                "catalog-pagination__link"))
            parsing_page = ParsingPage(site['item_element_class_name'], site['item_parameters_class'])
            while catalogue != None:
                items.extend(parsing_page.get_parse_items_selenium(catalogue))
                catalogue = paginator.page_change_algorithm.get_next_page()
            print('Hello')
    finally:
        Driver.get_instance().quit()



item_price_obj = ItemPrice(6, 200, 1)

item_price_repository = ItemPriceRepository()

item_price_repository.add(item_price_obj)

'''



