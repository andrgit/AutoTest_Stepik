from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Код который считывает значение х, и отправляет в функцию для вычисления. и возвр
    #x_element = browser.find_element_by_ * (selector)
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    #считываем строку и вводит туда значение полученное из функции
    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(y)

    # Выбираем checkbox- I'm the robot
    button_robCB = browser.find_element_by_id("robotCheckbox")
    button_robCB.click()

    # Выбираем radiobutton- "Robots rule!"
    button_RR = browser.find_element_by_id("robotsRule")
    button_RR.click()

    # Нажимаем кнопку Submit
    button_submit = browser.find_element_by_css_selector("button.btn")
    button_submit.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(10)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
