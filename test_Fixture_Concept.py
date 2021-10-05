from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest

"""
# code for set up of the setup and teardown method 

driver = None

def setup_module(module):
   global driver
   driver = webdriver.Chrome(ChromeDriverManager().install())
   driver.implicitly_wait(10)
   driver.delete_all_cookies()
   driver.get("https://www.google.com")

def teardown_module(module):
   driver.close()

def test_google_title():
   assert driver.title == "Google"

def test_google_url():
   assert driver.current_url == "https://www.google.com/"
"""


driver = None

@pytest.fixture(scope='module')
def init_driver():
   global driver
   print("--------------setup--------------")
   driver = webdriver.Chrome(ChromeDriverManager().install())
   driver.implicitly_wait(10)
   driver.get('https://www.google.com')
   yield
   print("--------------teardown------------")
   driver.close()

"""
# First way of using fixture
def test_google_title(init_driver):
   assert driver.title == "Google"

def test_google_url(init_driver):
   assert driver.current_url == "https://www.goole.com/"
"""

# Second way of using fixture
@pytest.mark.usefixtures("init_driver")
def test_google_title():
   assert driver.title == "Google"

@pytest.mark.usefixtures('init_driver')
def test_google_url():
   assert driver.current_url == "http://www.google.com"

