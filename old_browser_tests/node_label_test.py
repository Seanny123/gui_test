import os
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains

os.environ["SELENIUM_SERVER_JAR"] = "selenium-server-standalone-2.45.0.jar"

class NengoTitle(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
    
    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://localhost:8080")

        ensemble_elements = driver.find_elements_by_class_name("node")
        for e in ensemble_elements:
            text = e.get_attribute('textContent')
            assert text != ''
            print text
            
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()