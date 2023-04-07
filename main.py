import time

import requests
import fake_useragent
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get('https://mp24.bitrix24.ru/marketplace/app/10/')
elem = driver.find_element(By.ID, "login")
elem.clear()
elem.send_keys('anoxinconsult@mail.ru')
elem.send_keys(Keys.RETURN)
elem = driver.find_element(By.ID, "password")
elem.clear()
elem.send_keys('1qazxcde32WSX')
elem.send_keys(Keys.RETURN)

# Переключаемся на iframe
# iframe = driver.find_element(By.XPATH, '//iframe[1]')
# print(iframe.text)
driver.switch_to.frame('partner_application')

elem = driver.find_element(By.CLASS_NAME, 'main-ui-filter-search main-ui-filter-theme-default main-ui-filter-set-inside')
elem.clear()
elem.send_keys('1qazxcde32WSX')
elem.send_keys(Keys.RETURN)
time.sleep(10)
driver.close()

