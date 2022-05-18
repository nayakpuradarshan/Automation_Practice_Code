from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)

# hit url
driver.get("https://www.travolook.in/")
time.sleep(3)

# implicit wait
wait = WebDriverWait(driver, 10)

# Find From Location and enter location
From = wait.until(EC.presence_of_element_located((By.NAME, "flying_from_N")))
From.click()
From.send_keys("AMD,Ahmedabad International Airport")
From.send_keys(Keys.RETURN)

# Find To Location and enter location
To = wait.until(EC.presence_of_element_located((By.NAME, "flying_to_N")))
To.click()
To.send_keys("MAA,Chennai Airport")
time.sleep(2)
To.send_keys(Keys.RETURN)

# click on the Search Button
Search_Button = wait.until(EC.presence_of_element_located((By.ID, "searchengine_btn")))
Search_Button.click()

time.sleep(15)

# close driver
driver.close()

print("Succesed !")