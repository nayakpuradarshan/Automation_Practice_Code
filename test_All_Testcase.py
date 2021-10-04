from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# This will get the google home page
def test_google():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get('http://www.google.com')
    driver.quit()

# Check the facebook title
def test_facebook():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get('http://www.facebook.com')
    assert driver.title == "Facebook – log in or sign up"
    driver.quit()

# check the instagram title
def test_insta():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get('http://www.instagram.com')
    assert driver.title == "Instagram"
    driver.quit()

# Check the gmail title
def test_gmail():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get('http://www.gmail.com')
    assert driver.title == "Gmail"
    driver.quit()

# check the reddit title
def test_rediff():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get('http://www.rediff.com')
    assert driver.title == "Rediff.com: News | Rediffmail | Stock Quotes | Shopping"
    driver.quit()