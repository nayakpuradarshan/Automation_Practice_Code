from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import pytest
from time import sleep



@pytest.fixture(scope='class')
def init_chrome_driver(request):
    ch_driver = webdriver.Chrome(ChromeDriverManager().install())
    request.cls.driver = ch_driver
    yield
    ch_driver.close()

@pytest.fixture(scope='class')
def init_ff_driver(request):
    ff_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    request.cls.driver = ff_driver
    yield
    ff_driver.close()



#
@pytest.mark.usefixtures('init_chrome_driver')
class Base_chrome_test():
    pass

class Test_Google_Chrome(Base_chrome_test):

    def test_google_title_chrome(self):
        self.driver.get('http://www.google.com')
        assert self.driver.title == "Google"



@pytest.mark.usefixtures('init_ff_driver')
class Base_Firefox_test():
    pass

class Test_Google_Firefox(Base_Firefox_test):

    def test_google_title_firefox(self):
        self.driver.get('http://www.google.com')
        assert self.driver.title == "Google"
