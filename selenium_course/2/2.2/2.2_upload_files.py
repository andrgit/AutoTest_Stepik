from selenium import webdriver
import time
import os

try:  # Открываем необходимую ссылку
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)


    #Вводим имя,фамилия,email
    input_firstname = browser.find_element_by_name("firstname")
    input_firstname.send_keys("Ivan")
    input_lastname = browser.find_element_by_name("lastname")
    input_lastname.send_keys("Ivanov")
    input_email = browser.find_element_by_name("email")
    input_email.send_keys("123@123.com")

    # Нажимаем кнопку Choose file
    # button_file = browser.find_element_by_css_selector("//*[@id='file']")
    # button_file = browser.find_element_by_css_selector("file.upload.button")
    # button_file.click()

    # загрузить файл
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'skazka_info')  # добавляем к этому пути имя файла
    button_file = browser.find_element_by_id("file")
    button_file.send_keys(file_path)


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
