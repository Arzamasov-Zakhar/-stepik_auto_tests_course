import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip
import os
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, '1.txt')


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

with webdriver.Chrome() as browser:
    browser.get(link)

    button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    browser.find_element(By.CLASS_NAME, "btn-primary").click()

    browser.find_element(By.ID, "answer").send_keys(calc(browser.find_element(By.CSS_SELECTOR, "[id='input_value']").text))
    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    pyperclip.copy(browser.switch_to.alert.text.split(': ')[-1])
