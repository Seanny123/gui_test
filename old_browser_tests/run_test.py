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
        driver.implicitly_wait(5)
        actions = ActionChains(driver)
        driver.get("http://localhost:8080")

        button = driver.find_element_by_css_selector('.play-pause-button')
        actions.click(on_element=button)
        actions.perform()

        time = driver.find_element_by_id("VIZ.SimControl.ticks_div")
        time_val = time.get_attribute('textContent')

        assert time_val != 0.00

        actions.click(on_element=button)
        actions.perform()

        window = driver.find_element_by_id('VIZ.SimControl.shown_div')
        actions.drag_and_drop_by_offset(window, xoffset=-100, yoffset=0).perform()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
