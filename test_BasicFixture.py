from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time

driver = None

@pytest.fixture(scope="module")
def init_module():
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    yield
    driver.quit()

def test_google_logi(init_module):
    assert driver.title == "Google"

def test_gooel_url(init_module):
    url = driver.get("https://www.google.com/")
    assert driver.current_url == url
