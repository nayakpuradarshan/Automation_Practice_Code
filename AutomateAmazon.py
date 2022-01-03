import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import
from selenium.webdriver.support import expected_conditions as EC
import time


driver = None
wait = None

@pytest.fixture(scope='module')
def init_driver():
    global driver
    global wait
    print("--------------setup--------------")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.amazon.in")
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))

    yield
    print("--------------teardown-----------")
    print("DONE")
    driver.close()

def test_title(init_driver):
    """Check title of the amazon"""
    assert driver.title == "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in"

def test_url(init_driver):
    """Check url of the home page"""
    assert driver.current_url == 'https://www.amazon.in/'

def test_SearchField(init_driver):
    """Finding a search button"""
    search_button = driver.find_element(By.ID, "twotabsearchtextbox")
    time.sleep(10)
    search_button.click()
    search_button.clear()

def test_SearchMobile(init_driver):
    """Search availabel samsung phones"""
    search_button = driver.find_element(By.ID, "twotabsearchtextbox")
    time.sleep(10)
    search_button.send_keys("Samsung Phones")
    search_button.send_keys(Keys.RETURN)
    driver.back()

def test_SearchTvs(init_driver):
    """Search available Tvs"""
    search_button = driver.find_element(By.ID, "twotabsearchtextbox")
    time.sleep(10)
    search_button.send_keys("Smart Tvs")
    search_button.send_keys(Keys.RETURN)
    driver.back()

def test_SearchAcs(init_driver):
    """Check available Air conditions"""
    search_button = driver.find_element(By.ID, "twotabsearchtextbox")
    time.sleep(10)
    search_button.send_keys("Air Conditions")
    search_button.send_keys(Keys.RETURN)
    driver.back()