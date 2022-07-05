from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form")
    PRODUCT_PRICE = (By.CSS_SELECTOR,'.col-sm-6>.price_color')
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_NAME = (By.CSS_SELECTOR, "div.alertinner  strong")
    MESSAGE_PRICE =  (By.CSS_SELECTOR, 'div.alertinner p strong')