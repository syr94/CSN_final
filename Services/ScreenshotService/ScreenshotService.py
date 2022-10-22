#from PIL import Image
from numpy import full
from Driver.Driver import Driver
import re
import sys
import os

class ScreenshotService:

    def __init__(self, driver = Driver.get_instance()):
        self._driver = driver

    def save_screenshot(self,
            item_container,
            page_url : str,
            item_articul):
        try:
            url_list = re.sub(r"(https?://)?(www)?", "", page_url).split('/')
            main_folder = url_list[0]
            item_folder = url_list[-1]
            location = item_container.location
            size = item_container.size
            full_foler_path = "/home/$USER/Images/parser/{0}/{1}".format(
                main_folder,
                item_folder
            )
            if not os.path.exists(full_foler_path):
                os.makedirs(full_foler_path)
            sreenshot_path = full_foler_path + "/{}.png".format(item_articul)
            self._driver.save_screenshot(sreenshot_path)
            item_x_coordinnate = location['x']
            item_y_coordinate = location['y']
            width = location['x']+size['width']
            height = location['y']+size['height']
#            im = Image.open(sreenshot_path)
#            im = im.crop((int(item_x_coordinnate), int(item_y_coordinate), int(width), int(height)))
#            im.save('element.png')
        except:
            e = sys.exc_info()[1]
            print(e.args[0])