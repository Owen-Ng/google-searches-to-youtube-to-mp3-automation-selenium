from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Go on google and make a search and look for what we want like the names of the music you are looking for


class namesCollections(object):
    def __init__(self):
        PATH = "C:\Program Files (x86)\chromedriver.exe"
        option = webdriver.ChromeOptions()
        option.add_experimental_option(
            "excludeSwitches", ["enable-automation"])
        option.add_experimental_option('useAutomationExtension', False)
        option.add_extension("extension_1_35_2_0.crx")

        # For ChromeDriver version 79.0.3945.16 or over
        option.add_argument('--disable-blink-features=AutomationControlled')
        self.driver = webdriver.Chrome(executable_path=PATH, options=option)
        self.names = []

    def makeTheSearch(self, searchinput):
        self.driver.get("https://google.com")

        search = self.driver.find_element_by_name("q")  # search on google.com

        search.send_keys(searchinput)

        search.send_keys(Keys.RETURN)
        try:
            names = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(
                    (By.CLASS_NAME, "bVj5Zb"))
                # EC.presence_of_elements_located((By.CLASS_NAME, "KKHQ8c"))
            )
            for name in names:
                self.names.append(name.text)

            print(self.names)
        except:
            self.driver.quit()

    def getNames(self):
        return self.names

    def empty(self):
        self.names = []


# test = namesCollections()
# test.makeTheSearch("worship song")
# print(test.getNames())
