from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time

browser=webdriver.Chrome()
browser.get('https://www.wildberries.ru/')

# ------------------------ Поиск и выбор товара -------------------------

search = browser.find_element(by=By.ID, value='searchInput')
time.sleep(1)
search.send_keys('игрушка')
time.sleep(2)
search.send_keys(Keys.ENTER)
time.sleep(2)

item = browser.find_elements(By.CLASS_NAME, 'product-card')
item[0].click()
time.sleep(3)
