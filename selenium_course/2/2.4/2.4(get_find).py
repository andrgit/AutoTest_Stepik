from selenium import webdriver
import time


try:  # Открываем необходимую ссылку
    link = "http://suninjuly.github.io/wait1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # говорим WebDriver искать каждый элемент в течение 5 секунд
    # browser.implicitly_wait(5)


    #Поиск кнопки Verify и нажать на неё
    button = browser.find_element_by_id("verify")
    button.click()

    #Ищем на странице надпись подтверждения
    message = browser.find_element_by_id("verify_message")
    assert "successful" in message.text

    time.sleep(10)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()