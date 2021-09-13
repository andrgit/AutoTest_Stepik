from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

#Функция вычисляет выражение
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:  # Открываем необходимую ссылку
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # считать значение переменной Х и посчитать в функции число
    x_element = browser.find_element_by_id("input_value")
    x_cifra = x_element.text
    def_result = calc(x_cifra)

    #Вводим ответ в нужную строку
    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(def_result)

    # Выбираем checkbox- I'm the robot
    button_robCB = browser.find_element_by_id("robotCheckbox")
    button_robCB.click()

    #делаем прокрутку вниз
    browser.execute_script("window.scrollBy(0, 200);")

    # Выбираем radiobutton- "Robots rule!"
    button_RR = browser.find_element_by_id("robotsRule")
    button_RR.click()

    # Нажимаем кнопку Submit
    button_submit = browser.find_element_by_css_selector("button.btn")
    button_submit.click()

    # ждем загрузки страницы
    time.sleep(10)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
