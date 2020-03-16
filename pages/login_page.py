from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def check_login_page(self, language):
        assert "login.gaijin.net/" + language in self.browser.current_url, "Wrong login page"


    def login(self, email, password):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL_INPUT), "Login email input is not presented"
        email_input = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL_INPUT)
        email_input.send_keys(email)

        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD_INPUT), "Login password input is not presented"
        password_input = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD_INPUT)
        password_input.send_keys(password)

        time.sleep(2)

        assert self.is_element_present(*LoginPageLocators.LOGIN_AUTHORIZATION_BUTTON), "Login button is not presented"
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_AUTHORIZATION_BUTTON)
        login_button.click()

        assert self.is_element_present(*LoginPageLocators.LOGIN_CHOOSE_ACCOUNT_LINK), "Choose account is not presented"
        choose_account_link = self.browser.find_element(*LoginPageLocators.LOGIN_CHOOSE_ACCOUNT_LINK)
        choose_account_link.click()


    def check_account_page(self, language):
        assert "login.gaijin.net/" + language + "/profile/settings/security/" in self.browser.current_url, "Wrong profile page"
