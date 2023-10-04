from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time

browser=webdriver.Chrome()
browser.get('https://www.wildberries.ru/')

# ------------------  Смена валюты --------------------

time.sleep(2)
currency = browser.find_element(by=By.CLASS_NAME, value="simple-menu__currency")
currency.click()
currency = browser.find_element(by=By.CLASS_NAME, value="radio-with-text:nth-child(10) .radio-with-text__language")
currency.click()
time.sleep(3)
