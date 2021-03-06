from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def should_be_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        basket_name = self.browser.find_element(*ProductPageLocators.MESSAGE_NAME)
        assert product_name.text == basket_name.text, "The product name does not match"

    def should_be_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        basket_price = self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE)
        assert product_price.text == basket_price.text, "The product price does not match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
"Success message is presented, but should not be"

    def should_be_disapeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE),\
"Should be disappeared, but still is presented"
        