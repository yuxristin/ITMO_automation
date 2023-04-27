from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')

pole1 = driver.find_element(By.CSS_SELECTOR, '#user-name')
if pole1 is None:
    print('Not find')
else:
    print('Got Element')

pole1 = driver.find_element(By.CSS_SELECTOR, '#password')
if pole1 is None:
    print('Not find')
else:
    print('Got Element')

button1 = driver.find_element(By.CSS_SELECTOR, '#login-button')
if pole1 is None:
    print('Not find')
else:
    print('Got Element')

