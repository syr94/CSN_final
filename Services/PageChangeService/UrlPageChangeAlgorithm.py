#import PageChangeAlgorithm
from Driver.Driver import Driver
from selenium.webdriver.common.by import By
from ParsingPage import ParsingPage
from config import sites
from Services.PageChangeService.Paginator import Paginator

class UrlPageChangeAlgorithm:#(PageChangeAlgorithm):

    def __init__(self,current_catalogue : str, adding_url_template : str, link_class_name : str, driver = Driver.get_instance()):
        self._link_class_name = link_class_name
        self._adding_url_tempalte = adding_url_template
        self._driver = driver
        self._current_catalogue = current_catalogue
        self._current_page = 1

    def get_next_page(self):
        self._current_page += 1
        result = False
        elements = self._driver.find_elements(by = By.CLASS_NAME, value = self._link_class_name)
        for element in elements:
            if element.get_attribute('href').endswith(self._adding_url_tempalte + str(self._current_page)):
                result = True
                break
        if result:
            return self._current_catalogue + self._adding_url_tempalte + str(self._current_page)
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