import os
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

os.environ["SELENIUM_SERVER_JAR"] = "selenium-server-standalone-2.45.0.jar"

class NengoTitle(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
    
    def test_search_in_python_org(self):
        driver = self.driver
        driver.implicitly_wait(10)
        actions = ActionChains(driver)

        driver.get("http://localhost:8000")
        elem = driver.find_element_by_id('menu_open')
        actions.click(elem)
        actions.perform()

        nothing = driver.find_element_by_css_selector('.nothinghere')

        # # element3.send_keys("blablablabla")
        # # element3.send_keys(Keys.RETURN)
        # # WebDriverWait(100)
        # element3.send_keys('blabla')
        # element3.send_keys(" more bla", Keys.ARROW_DOWN)
        



    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()