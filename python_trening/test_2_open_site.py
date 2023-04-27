from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.rambler.ru/')

icon = driver.find_element(By.CSS_SELECTOR, '#app > header > div > div > nav > div:nth-child(2) > a > span > span')
if icon is None:
    print('Not find')
else:
    print('Got Element')

icon = driver.find_element(By.CSS_SELECTOR, '#app > header > div > div > nav > div:nth-child(4) > a > span > span')
if icon is None:
    print('Not find')
else:
    print('Got Element')

icon = driver.find_element(By.CSS_SELECTOR, 'div.rc__miHwc > div > div:nth-child(1) > a')
if icon is None:
    print('Not find')
else:
    print('Got Element')

icon = driver.find_element(By.CSS_SELECTOR, '#app > div.rc__efrlb.rc-header > div > div.rc__781Li.rc__o-jux > div > form > input')
if icon is None:
    print('Not find')
else:
    print('Got Element')


