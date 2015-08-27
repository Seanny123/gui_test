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
import numpy as np

model = nengo.Network(label='Ensemble Array')
with model:
    # Make an input node
    sin = nengo.Node(output=lambda t: [np.cos(t), np.sin(t)], label="sin")

    # Make ensembles to connect
    A = nengo.networks.EnsembleArray(100, n_ensembles=2, label="A")
    B = nengo.Ensemble(100, dimensions=2, label="B")
    C = nengo.networks.EnsembleArray(100, n_ensembles=2, label="C")

    # Connect the model elements, just feedforward
    nengo.Connection(sin, A.input)
    nengo.Connection(A.output, B)
    nengo.Connection(B, C.input)

    # Setup the probes for plotting
    sin_probe = nengo.Probe(sin)
    A_probe = nengo.Probe(A.output, synapse=0.02)
    B_probe = nengo.Probe(B, synapse=0.02)
    C_probe = nengo.Probe(C.output, synapse=0.02)
"""

cfg = """
_viz_10 = nengo_viz.Value(a)
_viz_config[_viz_10].x = 5.45344e+10
_viz_config[_viz_10].y = 1.34055e+09
_viz_config[_viz_10].width = 200
_viz_config[_viz_10].height = 200
_viz_config[_viz_10].label_visible = True
_viz_config[_viz_10].miny = -1
_viz_config[_viz_10].maxy = 1
_viz_9 = nengo_viz.Value(a)
_viz_config[_viz_9].x = 4.55943e+10
_viz_config[_viz_9].y = 1.02806e+10
_viz_config[_viz_9].width = 200
_viz_config[_viz_9].height = 200
_viz_config[_viz_9].label_visible = True
_viz_config[_viz_9].miny = -1
_viz_config[_viz_9].maxy = 1
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

        network_elements = driver.find_elements_by_class_name("net")
        for n in network_elements:
            text = n.get_attribute('textContent')
            assert text != ''
            print text

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()



