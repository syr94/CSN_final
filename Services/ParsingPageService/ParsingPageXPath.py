from typing import ItemsView
from Driver.Driver import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Models.Item import Item
from Models.ItemPrice import ItemPrice
from Repository.ItemRepository import ItemRepository
from Repository.ItemPriceRepository import ItemPriceRepository
from config import sites
from Services.ScreenshotService.ScreenshotService import ScreenshotService

class ParsingPageXPath:

    def __init__(self,
            options : dict,
            articul_get,
            driver = Driver.get_instance()):
        self._driver =  driver
        self._item_container_xpath = options.pop('item_element_x_path')
        self._options = options
        self._articul_get = articul_get
        self._image_service = ScreenshotService(driver)
        self._item_repository  = ItemRepository()
        self._item_price_repository = ItemPriceRepository()


    def set_item_element_class_name(self, item_element_class_name : str) -> None:
        self._item_element_class_name = item_element_class_name

    def set_item_parameters_classes(self, item_parameters_classes : dict) -> None:
        self._item_parameters_classes = item_parameters_classes

    def parse_all_attributes_from_element(self, item_container):
        parsed_attributes = {}
        for option in self._options:
            item_attribute = item_container.find_element(by=By.XPATH, value=self._options[option]).text
            parsed_attributes[option] = item_attribute

     #   item = Item(parsed_attributes['item_title_container_class'], parsed_attributes['item_price_container_class'])
        return 	parsed_attributes

    def parse_page(self, page_url : str) -> list:
        items_list = []
        items_price_list = []
        self._driver.get(page_url)
        xpathWait = self._item_container_xpath
        if xpathWait != '':
            WebDriverWait(self._driver, 1).until(EC.presence_of_element_located((By.XPATH, xpathWait)))
        print(self._driver.execute_script("return navigator.userAgent"))
        item_containers = self._driver.find_elements(by=By.XPATH, value=self._item_container_xpath)
        for item_container in item_containers:
            articul = self.get_articul_for_item(item_container)
            url = self.get_url_for_item(item_container)
            # TODO: fix this shit
            #self._image_service.save_screenshot(item_container, page_url, articul)
            item_attributes = self.parse_all_attributes_from_element(item_container)
            item = Item(
                id = articul, 
                name = item_attributes['item_title_container_class'],
                url = url)
            item_price = ItemPrice(
                item_id = articul,
                price = item_attributes['item_price_container_class'],
                parse_state_id= 1)
            self._item_repository.update(item)
            self._item_price_repository.update(item_price)
            items_list.append(item)
            items_price_list.append(item_price)
        return items_list
    
    def get_articul_for_item(self, item_container):
        """Getting articul for item from site. This articul will be used as id
        :param item_container: web element of item
        :return str: articul 
        """
        return self._articul_get.get_articul(item_container)
    
    def get_url_for_item(self, item_container):
        return self._articul_get.get_url(item_container)