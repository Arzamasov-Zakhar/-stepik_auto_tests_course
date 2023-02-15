import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"

with webdriver.Chrome() as browser:
    browser.get(link)
    x_elem = browser.find_element(By.CSS_SELECTOR, "[id='treasure']")
    x = x_elem.get_attribute('valuex')
    y = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "[type='checkbox']").click()
    browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']").click()
    browser.find_element(By.CLASS_NAME, "btn-default").click()

    time.sleep(10)
    alert = browser.switch_to.alert
    print(alert.text)