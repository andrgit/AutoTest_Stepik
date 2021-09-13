import value as value
from selenium import webdriver
import time
#
# link = "http://suninjuly.github.io/simple_form_find_task.html"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     input_answer = browser.find_element_by_tag_name("input.form-control")
#     input_answer.send_keys("Ivan")
#     input2 = browser.find_element_by_name("last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element_by_class_name("form-control.city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element_by_id("country")
#     input4.send_keys("Russia")
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(20)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#
# # не забываем оставить пустую строку в конце файла

# import math
#
# link = "http://suninjuly.github.io/find_link_text"
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     button = browser.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
#     button.click()
#     input_answer = browser.find_element_by_tag_name("input.form-control")
#     input_answer.send_keys("Ivan")
#     input2 = browser.find_element_by_name("last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element_by_class_name("form-control.city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element_by_id("country")
#     input4.send_keys("Russia")
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(20)
#     # закрываем браузер после всех манипуляций
#     browser.quit()


# from selenium.webdriver.common.by import By
# import time
#
# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/huge_form.html")
#     elements = browser.find_elements(By.CSS_SELECTOR, "input")
#     for element in elements:
#         element.send_keys("Мой ответ")
#
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# import value as value
# from selenium import webdriver
# import time
#
# link = "http://suninjuly.github.io/find_xpath_form"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     input_answer = browser.find_element_by_tag_name("input.form-control")
#     input_answer.send_keys("Ivan")
#     input2 = browser.find_element_by_name("last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element_by_class_name("form-control.city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element_by_id("country")
#     input4.send_keys("Russia")
#     button = browser.find_element_by_xpath("//button[@type='submit']")
#     button.click()
#
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(20)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# не забываем оставить пустую строку в конце файла

##########Registration1
from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    # elements = browser.find_element_by_tag_name("div.first_block input.form-control")
    # for element in elements:
    #     element.send_keys("Мой ответ")

    input1 = browser.find_element_by_tag_name("div.first_block input.form-control.first")
    input1.send_keys("Ivan")

    input2 = browser.find_element_by_tag_name("div.first_block input.form-control.second")
    input2.send_keys("Petrov")

    input3 = browser.find_element_by_tag_name("div.first_block input.form-control.third")
    input3.send_keys("123@ru.ru")

    #input2 = browser.find_element_by_name("last_name")
    # input3 = browser.find_element_by_tag_name("input.form-control.third")
    # input3.send_keys("Smolensk")
    # input4 = browser.find_element_by_id("country")
    # input4.send_keys("Russia")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

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

