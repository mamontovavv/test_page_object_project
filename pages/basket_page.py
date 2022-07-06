from .base_page import BasePage
from .locators import BasketPageLocators


from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

class BasketPage(BasePage):
    def should_be_no_products_in_basket(self):
         assert self.are_no_products_in_basket(*BasketPageLocators.ITEMS_TO_BUY), \
"Products are presented, but should not be"

    def should_be_message_about_empty_basket(self):
      assert self.is_message_about_empty_basket(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
"Message about empty basket is not presented"
