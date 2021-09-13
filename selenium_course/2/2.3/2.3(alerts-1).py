from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:  # Открываем необходимую ссылку
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #Нажимаю на кнопку на экране
    button_submit = browser.find_element_by_css_selector("button.btn")
    button_submit.click()

    #Переключаемся на алерт и нажимаем ок
    confirm = browser.switch_to.alert
    confirm.accept()

    # Код который считывает значение х, и отправляет в функцию для вычисления. и возвр
    # x_element = browser.find_element_by_ * (selector)
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    # считываем строку и вводит туда значение полученное из функции
    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(y)

    # Нажимаем кнопку Submit
    button_submit = browser.find_element_by_css_selector("button.btn")
    button_submit.click()


    time.sleep(10)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
