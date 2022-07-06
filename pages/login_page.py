from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес      
        assert "/login" in self.browser.current_url, "login is absent in current url"


    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        # принимает две строки и регистрирует пользователя. Реализуйте его, описав соответствующие элементы страницы.
          email_input = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
          email_input.send_keys(email)
          password_input = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
          password_input.send_keys(password)
          confirm_password_input = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_INPUT)
          confirm_password_input.send_keys(password)
          register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
          register_button.click()
