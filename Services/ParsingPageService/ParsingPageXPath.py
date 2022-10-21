from typing import ItemsView
from Driver.Driver import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Models.Item import Item
from config import sites

class ParsingPageXPath:

    def __init__(self,
            item_element_class_name  : str,
            item_parameters_classes : dict,
            driver = Driver.get_instance()):
        self._driver =  driver
        self._item_element_class_name = item_element_class_name
        self._item_parameters_classes = item_parameters_classes


    def set_item_element_class_name(self, item_element_class_name : str) -> None:
        self._item_element_class_name = item_element_class_name

    def set_item_parameters_classes(self, item_parameters_classes : dict) -> None:
        self._item_parameters_classes = item_parameters_classes

    # TODO : Переписать под паттерн стратегия
    def parse_all_attributes_from_element(self, item_container):
        parsed_attributes = {}
        for item_parameter_class in self._item_parameters_classes:
            item_attribute = [value.text for value in item_container.find_elements(by=By.CLASS_NAME, value=self._item_parameters_classes[item_parameter_class])]
            parsed_attributes[item_parameter_class] = item_attribute

        item = Item(parsed_attributes['item_title_container_class'], parsed_attributes['item_price_container_class'])
        return 	item

   # TODO : Переписать под паттерн стратегия
    def parse_page(self, page_url : str) -> list:
        parsed_page_items = []
        self._driver.get(page_url)
        xpathWait="//div[contains(@class, '{}')]".format(self._item_element_class_name)
        if xpathWait != '':
            WebDriverWait(self._driver, 1).until(EC.presence_of_element_located((By.XPATH, xpathWait)))
        print(self._driver.execute_script("return navigator.userAgent"))
        item_containers = self._driver.find_elements(by=By.CLASS_NAME, value=self._item_element_class_name)
        for item_container in item_containers:
            parsed_page_items.append(self.parse_all_attributes_from_element(item_container))
			#			screenshot = self.driver.save_screenshot(screen_name)
        return parsed_page_items