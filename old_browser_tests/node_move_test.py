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
        action_chains = ActionChains(driver)
        driver.get("http://localhost:8080")

        node_elements = driver.find_elements_by_class_name("node")
        for e in node_elements:
            action_chains.drag_and_drop_by_offset(e, xoffset=2, yoffset=2).perform()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()