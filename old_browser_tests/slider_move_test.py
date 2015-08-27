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
        driver.implicitly_wait(5)
        actions = ActionChains(driver)

        driver.get("http://localhost:8080")
        elem1 = driver.find_element_by_css_selector('div.graph:nth-child(4) > button:nth-child(2)')
        actions.drag_and_drop_by_offset(elem1, xoffset=0, yoffset=-25).perform()
       
        elem2 = driver.find_element_by_css_selector('button.btn:nth-child(3)')
        actions.drag_and_drop_by_offset(elem2, xoffset=0, yoffset=25).perform()

        text1 = elem1.get_attribute('textContent')
        assert text1 != "0.00"

        text2 = elem2.get_attribute('textContent')
        assert text2 != "0.00"

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()


    