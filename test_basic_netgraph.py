from selenium.webdriver import ActionChains

# test the basic attributes of the components

# test browser resizing

# conbine the labels and movement into a for-loop
nengo_object_list = ["ens", "node", "net"]

def test_pageload(driver):
    # assert "localhost" in driver.page_source
    assert "nengo.js" in driver.page_source
"""
def test_node_labels(driver):
    nodes = driver.find_elements_by_class_name("node")
    for n in nodes:
        n_text = n.get_attribute('textContent')
        assert n_text != ''

def test_node_movement(driver):
    actions = ActionChains(driver)
    nodes = driver.find_elements_by_class_name("node")
    for node in nodes:
        prev_location = node.location
        actions.drag_and_drop_by_offset(node, xoffset=6, yoffset=5).perform()
        assert prev_location['x'] - node.location['x'] == 6
        assert prev_location['y'] - node.location['y'] == 5

def test_node_slider(driver):
    actions = ActionChains(driver)
    node = driver.find_element_by_css_selector("g.node:nth-child(3)")
    node.click()

    menu = driver.find_element_by_id('GUI_popup_menu')
    buttons = driver.find_elements_by_css_selector('#GUI_popup_menu button')
    for button in buttons:
        text = button.get_attribute('textContent')
        if text == 'Slider':
            button.click()
            break

def test_ensemble_labels(driver):
    ensembles = driver.find_elements_by_class_name("ens")
    for ens in ensembles:
        e_text = ens.get_attribute('textContent')
        assert e_text != ''

def test_ensemble_movement(driver):
    actions = ActionChains(driver)
    ensembles = driver.find_elements_by_class_name("ens")
    for ens in ensembles:
        actions.drag_and_drop_by_offset(ens, xoffset=5, yoffset=5).perform()
"""