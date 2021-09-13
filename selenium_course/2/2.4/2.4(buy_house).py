from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")



    # говорим Selenium проверять в течение 5 секунд, пока цена не будет 100
    button = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    # Нажимаем кнопку Book
    button_book = browser.find_element_by_id("book")
    button_book.click()

    # Код который считывает значение х, и отправляет в функцию для вычисления. и возвр
    # x_element = browser.find_element_by_ * (selector)
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    # считываем строку и вводит туда значение полученное из функции
    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(y)

    # Нажимаем кнопку Submit внизу после формулы
    button_submit = browser.find_element_by_id("solve")
    button_submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
