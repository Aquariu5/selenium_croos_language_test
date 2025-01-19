from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

def test_add_to_basket_button_is_displayed(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    assert browser.find_element(By.CSS_SELECTOR, '.basket-mini a'), "Goto in basket butto not found"


