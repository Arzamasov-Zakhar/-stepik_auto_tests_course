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

link = "http://suninjuly.github.io/redirect_accept.html"

with webdriver.Chrome() as browser:
    browser.get(link)
    browser.find_element(By.ID, "button").click()
