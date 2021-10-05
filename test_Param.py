# This code will explain you parameterizing concept
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import pytest
import time

@pytest.mark.usefixtures('init_driver')
class BaseTest:
    pass

class TestHubSpot(BaseTest):

    @pytest.mark.parametrize(
                            "username, password",
                            [("darshan@gmail.com", "darshan@123"),
                             ("darsh@gmail.com", "darsh@123")
                             ]
                            )
    def test_login(self, username, password):
        """
        This methos is used to login into the hub spot application
        :param username:
        :param password:
        :return:
        """
        self.driver.get("https://www.instagram.com")
        time.sleep(3)
        self.driver.find_element(By.NAME, "username").send_keys("user_username")
        self.driver.find_element(By.NAME, "password").send_keys("user_password")
        self.driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[3]").click()