from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_xpath_form"

with webdriver.Chrome() as browser:
    browser.get(link)
    input1 = browser.find_element(By.NAME, "first_name")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, "firstname")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")

    button = browser.find_element(By.XPATH, "//body/div/form/div[6]/button[3]")
    button.click()


    alert = browser.switch_to.alert
    print(alert.text)
