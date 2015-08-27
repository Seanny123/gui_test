import os
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

os.environ["SELENIUM_SERVER_JAR"] = "selenium-server-standalone-2.45.0.jar"

class NengoTitle(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
    
    def test_search_in_python_org(self):
        driver = self.driver
        driver.implicitly_wait(5)
        actions = ActionChains(driver)
        driver.get("http://localhost:8080")

        slider = driver.find_element_by_css_selector('.graph')
        actions.click(on_element=slider)
        actions.perform()

        menu = driver.find_element_by_id('VIZ_popup_menu')
        buttons = driver.find_elements_by_css_selector('#VIZ_popup_menu button')
        for button in buttons:
            text = button.get_attribute('textContent')
            if text == 'Remove':
                button.click()

        try:
            x = driver.find_element_by_css_selector('.graph')
        except:
            pass
        else:
            assert 'Graph was not removed' in driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
