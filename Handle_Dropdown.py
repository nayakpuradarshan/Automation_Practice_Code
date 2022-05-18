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

# get the facebook login page
driver.get("https://www.facebook.com")

wait = WebDriverWait(driver, 10)

create_account = wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()= 'Create New Account']")))
create_account.click()

month = wait.until(EC.presence_of_element_located((By.ID, "month")))
monthDD=Select(month)


"""
# March - select by index number
monthDD.select_by_index(2)
time.sleep(2)

# Aug - Select by value
monthDD.select_by_value("8")
time.sleep(2)

#  Dec - Visible text
monthDD.select_by_visible_text("Dec")
time.sleep(5)
"""


ddlist = monthDD.options
print(ddlist)



driver.close()