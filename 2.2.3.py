import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pyperclip


link = "https://suninjuly.github.io/selects1.html"

with webdriver.Chrome() as browser:
    browser.get(link)
    x = browser.find_element(By.ID, "num1")
    y = browser.find_element(By.ID, "num2")
    sum1 = int(x.text) + int(y.text)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(sum1))
    browser.find_element(By.CSS_SELECTOR, "button").click()


    alert = browser.switch_to.alert
    addToClipBoard = alert.text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)
