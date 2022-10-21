from os import O_NONBLOCK
from pandas import options
import undetected_chromedriver.v2 as uc
from selenium_stealth import stealth
import selenium.webdriver.chrome as driver
import time

# TODO Переделать uc под проект
class Driver(object):
        __instance = None

        def __init__(self):
            if not Driver.__instance:     
                print(" __init__ method called..")
            else:
                print("Instance already created:", self.get_instance())
                
        @classmethod
        def get_instance(cls):
            if not cls.__instance:
                option = uc.ChromeOptions()
                cls.__instance = uc.Chrome(
                    version_main = 102,
                    options=option
                    )
                
                stealth(cls.__instance,
                    languages=["en-US", "en"],
                    vendor="Google Inc.",
                    platform="Win32",
                    webgl_vendor="Intel Inc.",
                    renderer="Intel Iris OpenGL Engine",
                    fix_hairline=True,
                )
            return cls.__instance
'''
s = Driver().getInstance() ## class initialized, but object not created
print("Object created", Driver.getInstance()) # Object gets created here
url = "https://bot.sannysoft.com/"
s.get("https://market.yandex.ru/product--smartfon-apple-iphone-13/1414986413/reviews")
time.sleep(7)

s.quit()
s1 = Driver() ## instance already created
'''