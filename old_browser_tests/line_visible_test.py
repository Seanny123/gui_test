import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

os.environ["SELENIUM_SERVER_JAR"] = "selenium-server-standalone-2.45.0.jar"

code = """"
import nengo
model = nengo.Network(label="My Network")
with model:
    input = nengo.Node([0, 0])

    a = nengo.Ensemble(100, dimensions=2, label="My Ensemble")
    nengo.Probe(a)
    nengo.Probe(a.neurons)

    nengo.Connection(input, a)
"""

cfg = """
_viz_net_graph = nengo_viz.NetGraph()
_viz_sim_control = nengo_viz.SimControl()
_viz_config[a].pos=(50494793.30117646, 2998995.532436888)
_viz_config[a].size=(0.15151515151515152, 0.25)
_viz_config[input].pos=(-99747909.63381924, 5646706.0920250695)
_viz_config[input].size=(18211236.770816773, 74500513.76656447)
_viz_config[model].pos=(286145497.1899674, 359796645.4472506)
_viz_config[model].size=(1.6778407827795093e-09, 1.6778407827795093e-09)
_viz_config[model].expanded=True
_viz_config[model].has_layout=True
"""

class NengoTitle(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()    # Chrome('/Users/peterblouw/git/nengo_viz/browser_tests/chromedriver')
    
    def test_search_in_python_org(self):
        driver = self.driver
        driver.implicitly_wait(10)
        actions = ActionChains(driver)
        driver.get("http://localhost:8080")


        ens = driver.find_element_by_class_name('ens')
        ens.click()

        menu = driver.find_element_by_id('VIZ_popup_menu')
        buttons = driver.find_elements_by_css_selector('#VIZ_popup_menu button')
        for button in buttons:
            text = button.get_attribute('textContent')
            if text == 'Value':
                button.click()
                break

        graph = driver.find_element_by_css_selector(".graph")
        actions.drag_and_drop_by_offset(graph, xoffset=-15, yoffset=15).perform()

        play_button = driver.find_element_by_id('VIZ.SimControl.play_button')
        play_button.click()

        time.sleep(3)
        line = driver.find_element_by_css_selector("path.line:nth-child(1)")
        
        data = line.rect 
        print data       
        test_val = data['height'] + data['width']
        assert test_val != 0

        block = driver.find_element_by_id("BlockTestCompletion")


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()



