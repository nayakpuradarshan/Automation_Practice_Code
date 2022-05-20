from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(10)

# Open below url
driver.get("https://www.facebook.com")

# Created the explicit wait
wait = WebDriverWait(driver, 10)

# Click on the create New Account button
wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()= 'Create New Account']"))).click()
time.sleep(5)

# find element with name day
Date = wait.until(EC.presence_of_element_located((By.ID, "day")))
DateDD = Select(Date)

# select element with index number three
DateDD.select_by_index(3)
time.sleep(3)

# select element with text 10
DateDD.select_by_visible_text("10")
time.sleep(4)

# here you can practice more about select



driver.close()