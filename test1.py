from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time

browser=webdriver.Chrome()
browser.get('https://www.wildberries.ru/')

# ------------------  Переход на страницу "Корзина" --------------------

time.sleep(2)
basket = browser.find_element(by=By.CLASS_NAME, value="navbar-pc__icon--basket")
basket.click()
time.sleep(3)
