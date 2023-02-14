import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyperclip
import os
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, '1.txt')


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/file_input.html"

with webdriver.Chrome() as browser:
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter first name']").send_keys("Ivan")
    browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter last name']").send_keys("Petrov")
    browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter email']").send_keys("Petrov@mail.ru")

    browser.find_element(By.CSS_SELECTOR, "[id='file']").send_keys(file_path)
    browser.find_element(By.CLASS_NAME, "btn-primary").click()

    alert = browser.switch_to.alert
    addToClipBoard = alert.text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)
