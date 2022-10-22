from Services.SiteItemArticulGetService.ArticulGetAlgorithm import ArticulGetAlgorithm
from selenium.webdriver.common.by import By
from Driver.Driver import Driver

class ArticulGetByLink(ArticulGetAlgorithm):

    def __init__(self, options):
        self._link = options['item_card_link']

    
    def get_articul_from_block(self, block)-> str:
        articul_url  = block.find_element(by = By.CLASS_NAME, value = self._link).get_attribute('href')
        articul = articul_url.split('/')[-1].split('.')[0]
        return articul

    def get_item_url(self, block):
        item_url  = block.find_element(by = By.CLASS_NAME, value = self._link).get_attribute('href')
        return item_url