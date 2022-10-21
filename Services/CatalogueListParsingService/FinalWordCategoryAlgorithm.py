from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os
import sys
from Driver.Driver import Driver
pwd = os.path.dirname(sys.argv[0])
sys.path.append(pwd + "/../../Driver")
sys.path.append(pwd + "/../../")
#from Driver import Driver
from config import sites
from Repository.AlgorithmParameterRepository import AlgorithmParameterRepository
from Repository.AlgorithmRepository import AlgorithmRepository

class FinalWordCategoryAlgorithm:

    def __init__(self,
            main_page_url : str = '',
            ):
        algorithm_repository =  AlgorithmRepository()
        self.algorithm_id = algorithm_repository.find_one_by(
            by = "algorithm_class_name", 
            value = self.__class__.__name__
        ).algorithm_id
    
    def get_catalogue_list(self,
            main_page_url,
            site_city_id,
            driver: Driver = Driver.get_instance(),
            ):
        algorithmParameterRepository = AlgorithmParameterRepository()
        algorithm_parameters = algorithmParameterRepository.get_algorithm_parameters_name_values(self.algorithm_id, site_city_id)
        catalogue_element_xpath  = algorithm_parameters['catalogue_element_xpath']
        catalogue_list_item_xpath = algorithm_parameters['catalogue_list_item_xpath']
        driver.get(main_page_url)
        if catalogue_element_xpath != '':
            WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, catalogue_element_xpath)))
        item_containers = driver.find_elements(by=By.XPATH, value=catalogue_list_item_xpath)#.getAttribute("href")
        links = [item_container.get_attribute("href") for item_container in item_containers]
        valid_links = self.get_valid_links(links)
        return valid_links

	# TODO: продумать алгоритм этой шляпы без использования индексов
    def get_valid_links(self, links_list : list):
        links_list.sort()
        valid_links = []
        for index in range(1, len(links_list)):
            if (links_list[index].find(links_list[index-1]) == -1):
                valid_links.append(links_list[index-1])
        return valid_links
