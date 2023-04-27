from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')


pole1 = driver.find_element(By.CSS_SELECTOR, '#user-name')
if pole1 is None:
    print('Not find')
else:
    print('Got Element')

pole2 = driver.find_element(By.CSS_SELECTOR, '#password')
if pole2 is None:
    print('Not find')
else:
    print('Got Element')

button1 = driver.find_element(By.CSS_SELECTOR, '#login-button')
if button1 is None:
    print('Not find')
else:
    print('Got Element')

list = [pole1, pole1, button1]

def get_number_of_elements(list):
    count = 0
    for element in list:
        count += 1
    return count

print("Number of elements in the list: ", get_number_of_elements(list))

