from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)

# hit url
driver.get("https://www.skyscanner.co.in/")

# implicit wait
wait = WebDriverWait(driver, 10)

# Search hotel button and click on it
time.sleep(2)
hotels = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='skhot']/span")))
hotels.click()
driver.refresh()

# search on the Car Hits button and click on it
time.sleep(2)
car_hits = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='carhi']/span")))
car_hits.click()
time.sleep(2)

driver.refresh()

# close driver
driver.close()

print("Succesed !")