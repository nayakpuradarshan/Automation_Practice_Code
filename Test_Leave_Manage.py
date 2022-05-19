import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = None

@pytest.fixture(scope='module')
def init_driver():
    global driver
    print("--------------setup--------------")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(10)
    # driver.get("http://122.169.108.222:1016/")
    driver.get("http://192.168.6.106:1016/")

    # Enter Username
    wait = WebDriverWait(driver, 20)
    Username = wait.until(EC.presence_of_element_located((By.ID, "userName")))
    Username.click()
    Username.send_keys("admin")

    # Enter password
    Password = wait.until(EC.presence_of_element_located((By.ID, "password")))
    Password.click()
    Password.send_keys("123456")

    # click on the Login Button
    wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[2]/div/div[2]/form/div[3]/button"))).click()

    yield
    print("--------------teardown-----------")
    print("DONE")
    driver.close()


def test_HRManage(init_driver):

    wait = WebDriverWait(driver, 10)

    # Click on the HR Manage menu
    wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='HR Manage']"))).click()
    # Click on the Department menu
    wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()= ' Department']"))).click()
    driver.refresh()

    # Open the Add Department
    wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[1]/a"))).click()
    time.sleep(6)

    # Enter value in the Department Field
    wait.until(EC.presence_of_element_located((By.ID, "DepartmentMasters_MastName"))).send_keys("ABCD")

    # click on the Submit button
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()= ' Submit']"))).click()

    # now do refresh
    driver.refresh()
    time.sleep(10)












