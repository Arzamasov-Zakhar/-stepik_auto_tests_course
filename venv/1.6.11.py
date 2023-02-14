import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = " http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"


with webdriver.Chrome() as browser:
    for i in link, link2:
        browser.get(i)
        input1 = browser.find_element(By.XPATH, "//body/div/form/div/div/input")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, "//body/div/form/div/div[2]/input")
        input2.send_keys("Petrov")
        input2 = browser.find_element(By.XPATH, "//body/div/form/div/div[3]/input")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH, "//body/div/form/div[2]/div/input")
        input3.send_keys("Smolensk")
        input4 = browser.find_element(By.XPATH, "//body/div/form/div[2]/div[2]/input")
        input4.send_keys("Russia")

        button = browser.find_element(By.XPATH, "//body/div/form/button")
        button.click()
        time.sleep(3)

        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        assert "Congratulations! You have successfully registered!" == welcome_text

