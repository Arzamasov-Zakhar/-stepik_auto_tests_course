import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyperclip


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = " https://suninjuly.github.io/math.html"

with webdriver.Chrome() as browser:
    browser.get(link)
    x_elem = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
    x = x_elem.text
    y = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "[type='checkbox']").click()
    browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']").click()
    browser.find_element(By.CLASS_NAME, "btn-default").click()

    # time.sleep(2)
    alert = browser.switch_to.alert
    addToClipBoard = alert.text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)


