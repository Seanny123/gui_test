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
        actions = ActionChains(driver)

        driver.get("http://localhost:8000")

        # Test for text in editor
        inp_elem = driver.find_element_by_class_name('ace_text-input')
        text_elem = driver.find_element_by_class_name('ace_content')

        text1 = text_elem.get_attribute('textContent')

        assert "nengo.Network" in text1

        # Test for changes to text
        inp_elem.clear()
        inp_elem.send_keys('TESTING TEXT ENTRY')
        text2 = text_elem.get_attribute('textContent')

        assert "TESTING" in text2
  
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()