import os
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

os.environ["SELENIUM_SERVER_JAR"] = "selenium-server-standalone-2.45.0.jar"

class NengoTitle(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
    
    def test_search_in_python_org(self):
        driver = self.driver
        driver.implicitly_wait(5)
        actions = ActionChains(driver)
        driver.get("http://localhost:8080")

        value = driver.find_element_by_css_selector('.graph')
        actions.click(on_element=value)
        actions.perform()

        menu = driver.find_element_by_id('VIZ_popup_menu')
        buttons = driver.find_elements_by_css_selector('#VIZ_popup_menu button')
        for button in buttons:
            text = button.get_attribute('textContent')
            if text == 'Set range':
                button.click()
                WebDriverWait(driver, 5).until(EC.alert_is_present())
                alert = driver.switch_to_alert()
                alert.send_keys("-0.1,0.1")
                alert.accept()
                break
                
        tick = driver.find_element_by_css_selector('g.axis:nth-child(4) > g:nth-child(1)')
        text = tick.get_attribute('textContent')
        assert text == "-0.1"

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
