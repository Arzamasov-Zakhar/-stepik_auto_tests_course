import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyperclip


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://SunInJuly.github.io/execute_script.html"

with webdriver.Chrome() as browser:
    browser.get(link)
    browser.find_element(By.ID, "answer").send_keys(calc(browser.find_element(By.CSS_SELECTOR, "[id='input_value']").text))
    browser.find_element(By.CSS_SELECTOR, "[type='checkbox']").click()
    button = browser.find_element(By.CLASS_NAME, "btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']").click()
    browser.find_element(By.CLASS_NAME, "btn-primary").click()

    alert = browser.switch_to.alert
    addToClipBoard = alert.text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)
