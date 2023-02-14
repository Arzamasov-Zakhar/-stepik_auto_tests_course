from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # counter = 0 # счетчик количества заполняемых полей

    # Ваш код, который заполняет обязательные поля
    # list_label = browser.find_elements(By.TAG_NAME, "label") # список всех тегов label
    # list_input = browser.find_elements(By.TAG_NAME, "input") # список всех тегов input
    # for el, tx in zip(list_input, list_label): # перебераем паралельно элементы списков
    #     if "*" in tx.text: # если в тексте есть пометка на обязательное заполнение то:
    #         counter += 1 # добавляем к счетчику обязательных полей
    #         el.send_keys("Это обязательное поле") # заполняем такое поле
    first_name = browser.find_element(By.CSS_SELECTOR, '.first_block .first')
    first_name.send_keys("Это поле обязательно для заполнения")
    last_name = browser.find_element(By.CSS_SELECTOR, '.first_block .second')
    last_name.send_keys("Это поле обязательно для заполнения")
    email_name = browser.find_element(By.CSS_SELECTOR, '.first_block .third')
    email_name.send_keys("Это поле обязательно для заполнения")

    # for el in (first_name, last_name, email_name):
    #     el.send_keys("Это поле обязательно для заполнения")
        
    time.sleep(1)
    
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст и количество обязательных полей совпадает с текстом и количеством на странице сайта 
    assert "Congratulations! You have successfully registered!" == welcome_text #and counter == 3

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
