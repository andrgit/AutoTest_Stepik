import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_find_button_add_to_basket(browser):
    browser.get(link)
    time.sleep(30)
    button_basket = browser.find_element_by_css_selector("button.btn.btn-lg.btn-primary")
    assert button_basket, "Кнопка не найдена"
