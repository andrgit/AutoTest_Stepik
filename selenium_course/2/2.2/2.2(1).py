from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


def summa(x, y):
    return str(x + y)


try:  # Открываем необходимую ссылку
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # считать 2 значения и посчитать сумму через функцию
    element1 = browser.find_element_by_id("num1")
    element2 = browser.find_element_by_id('num2')
    itogo = summa(int(element1.text), int(element2.text))

    # импорт селект, находим пункт селект, и сразу выбираем текст с результатом itogo
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(itogo)  # ищем элемент с текстом "Python"

    # Нажимаем кнопку Submit
    button_submit = browser.find_element_by_css_selector("button.btn")
    button_submit.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(10)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
