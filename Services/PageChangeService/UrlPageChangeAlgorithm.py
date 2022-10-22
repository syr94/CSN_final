#import PageChangeAlgorithm
from Driver.Driver import Driver
from selenium.webdriver.common.by import By
from ParsingPage import ParsingPage
from config import sites
from Services.PageChangeService.Paginator import Paginator

class UrlPageChangeAlgorithm:#(PageChangeAlgorithm):

    def __init__(self,
            options : dict,
            driver = Driver.get_instance()):
        self._link_class_name = options['catalogue_pagination_link']
        self._adding_url_tempalte = options['catalogue_pagination_template']
        self._current_page = 1
        self._driver = driver

    @property
    def current_page(self) -> int:
        return self._current_page

    @current_page.setter
    def current_page(self, new_current_page : int = 1) -> None:
        self._current_page = new_current_page

    @property
    def driver(self) -> Driver:
        return self._driver

    @driver.setter
    def driver(self, new_driver : Driver) -> None:
        self._driver = new_driver

    def get_next_page(self,
        current_catalogue):
        self._current_page += 1
        result = False
        elements = self._driver.find_elements(by = By.CLASS_NAME, value = self._link_class_name)
        for element in elements:
            if element.get_attribute('href').endswith(self._adding_url_tempalte + str(self._current_page)):
                result = True
                break
        if result:
            return current_catalogue + self._adding_url_tempalte + str(self._current_page)
        self.current_page = 1
        return None
'''
paginator = UrlPageChangeAlgorithm(
    'https://set-tehniki.com/store/tele/televizory',
    "?page=",
    "catalog-pagination__link"
)
result = paginator.get_next_page()

print(result)

items = []

site = sites['set-tehniki']
paginator = Paginator(UrlPageChangeAlgorithm(
    'https://set-tehniki.com/store/kitchen/melkaya-bytovaya-tehnika/blendery',
    "?page=",
    "catalog-pagination__link"))
parsing_page = ParsingPage(site['item_element_class_name'], site['item_parameters_class'])
items.extend(parsing_page.get_parse_items_selenium("https://set-tehniki.com/store/kitchen/melkaya-bytovaya-tehnika/blendery"))
result = paginator.pageChangeAlgorithm.get_next_page()
print(result)
parsing_page = ParsingPage(site['item_element_class_name'], site['item_parameters_class'])
items.extend(parsing_page.get_parse_items_selenium(result))
'''