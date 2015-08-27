To run tests on the graphical user interface for Nengo, installation of 
selenium is required. Do 'pip install selenium', and for more info, see: 
https://selenium-python.readthedocs.org/installation.html

Next, you will need a .jar file for running the selenium webserver. This can 
be downloaded here (if it is not already present in the git repository):
http://selenium-release.storage.googleapis.com/2.45/selenium-server-standalone-2.45.0.jar

You will also need to have the Java Runtime Environment (JRE) installed:
http://www.oracle.com/technetwork/java/javase/downloads/jre8-downloads-2133155.html


RUNNING TESTS ON DIFFERENT BROWSERS
===================================

These instructions assume that you have installed the browser being tested.
The test described in example.py can be run on different browsers by 
incorporating the following changes:

Firefox:
Simply update the setUp method in the class NengoTitle as follows:

.. code:: python

	def setUp(self):
        self.driver = webdriver.Firefox()

Chrome: 
Chromedriver is required to create an instance of the Chrome Webdriver. It
can be downloaded at http://chromedriver.storage.googleapis.com/index.html?path=2.15/
Update the setUp method in this case to include the path to chromedriver:

 .. code:: python

	def setUp(self):
	    self.driver = webdriver.Chrome('path/chromedriver')

Safari:
A Safari extension is required to - follow these instructions to install it:

- Download http://central.maven.org/maven2/org/seleniumhq/selenium/selenium-safari-driver/2.43.1/selenium-safari-driver-2.43.1.jar
- Unzip it (just double click on it to do so). 
- In Finder, go to ../selenium-safari-driver-2.43.1/org/openqa/selenium/safari
- Double click "SafariDriver.safariextz"

A WebDriver extension should now be visible in Safari -> Preferences -> Extensions

Now, simply update the setUp method in example.py as follows:

.. code:: python

	def setUp(self):
        self.driver = webdriver.Safari()

All of these instructions assume that you have nengo, nengo_viz, and nengo_gui
installed in the same environment as selenium. You will also need to have
nengo_gui running in order for the test to pass successfully. 



