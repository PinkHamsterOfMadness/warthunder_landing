from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import LandingPageLocators
from .locators import RegistrationFormLocators
import time


class LandingPage(BasePage):
    def search_all_elements(self):
        assert self.is_element_present(
            *LandingPageLocators.LANDING_LANGUAGE_PICKER), "Language picker is not presented"
        assert self.is_element_present(
            *LandingPageLocators.LANDING_LOGO), "Landing logo is not presented"
        assert self.is_element_present(
            *LandingPageLocators.LANDING_SPECIAL_LOGO), "Landing special logo is not presented"
        assert self.is_element_present(
            *LandingPageLocators.LANDING_REGISTRATION_BUTON), "Landing registration button is not presented"
        assert self.is_element_present(
            *LandingPageLocators.LANDING_FOOTER_GAIJIN_LOGO), "Landing gaijin logo is not presented"
        assert self.is_element_present(
            *LandingPageLocators.LANDING_FOOTER_PC_LOGO), "Landing PC logo is not presented"
        assert self.is_element_present(
            *LandingPageLocators.LANDING_FOOTER_MAC_LOGO), "Landing MAC logo is not presented"
        assert self.is_element_present(
            *LandingPageLocators.LANDING_FOOTER_PS4_LOGO), "Landing PS4 logo is not presented"
        assert self.is_element_present(
            *LandingPageLocators.LANDING_FOOTER_GAMESCOM), "Landing gamescom logo is not presented"
        assert self.is_element_present(
            *LandingPageLocators.LANDING_FOOTER_PEGI), "Landing PEGI logo is not presented"
        assert self.is_element_present(
            *LandingPageLocators.LANDING_PRIVACY_POLICY_LINK), "Landing privacy policy link is not presented"
        assert self.is_element_present(
            *LandingPageLocators.LANDING_EULA_LINK), "Landing EULA link is not presented"
        assert self.is_element_present(
            *LandingPageLocators.LANDING_TERMS_OF_USE_LINK), "Landing terms of use link is not presented"

    def search_ru_customer_support_link(self):
        assert self.is_element_present(
            *LandingPageLocators.LANDING_CUSTOMER_SUPPORT_RU_LINK), "Landing customer support link is not presented"

    def search_en_customer_support_link(self):
        assert self.is_element_present(
            *LandingPageLocators.LANDING_CUSTOMER_SUPPORT_EN_LINK), "Landing customer support link is not presented"

    def open_registration_form(self):
        assert self.is_element_present(
            *LandingPageLocators.LANDING_REGISTRATION_BUTON), "Landing registration button is not presented"
        registration_button = self.browser.find_element(*LandingPageLocators.LANDING_REGISTRATION_BUTON)
        registration_button.click()

    def search_all_elements_registration_form(self):
        assert self.is_element_present(
            *RegistrationFormLocators.REGISTRATION_FORM), "Registration form is not presented"
        assert self.is_element_present(
            *RegistrationFormLocators.REGISTRATION_FORM_EXIT), "Registration form exit button is not presented"
        assert self.is_element_present(
            *RegistrationFormLocators.REGISTRATION_EMAIL_INPUT), "Registration form email input is not presented"
        assert self.is_element_present(
            *RegistrationFormLocators.REGISTRATION_PASSWORD_INPUT), "Registration form password input is not presented"
        assert self.is_element_present(
            *RegistrationFormLocators.REGISTRATION_NICKNAME_INPUT), "Registration form nickname input is not presented"
        assert self.is_element_present(
            *RegistrationFormLocators.REGISTRATION_PASSWORD_REPEAT_INPUT), "Registration form password repeat input is not presented"
        assert self.is_element_present(
            *RegistrationFormLocators.REGISTRATION_CAPTCHA_INPUT), "Registration form captcha input is not presented"
        assert self.is_element_present(
            *RegistrationFormLocators.REGISTRATION_CAPTCHA_RELOAD), "Registration form captcha reload is not presented"
        assert self.is_element_present(
            *RegistrationFormLocators.REGISTRATION_CAPTCHA_IMAGE), "Registration form captha image is not presented"
        assert self.is_element_present(
            *RegistrationFormLocators.REGISTRATION_EULA_CHECKBOX), "Registration form EULA checkbox is not presented"
        assert self.is_element_present(
            *RegistrationFormLocators.REGISTRATION_EULA_LINK), "Registration form EULA link is not presented"
        assert self.is_element_present(
            *RegistrationFormLocators.REGISTRATION_TERMS_OF_USE_LINK), "Registration form Terms of use link is not presented"
        assert self.is_element_present(
            *RegistrationFormLocators.REGISTRATION_PRIVACY_POLICY_LINK), "Registration form pryvacy policy is not presented"
        assert self.is_element_present(
            *RegistrationFormLocators.REGISTRATION_SUBSCRIBE_CHECKBOX), "Registration form subscribe checkbox is not presented"
        assert self.is_element_present(
            *RegistrationFormLocators.REGISTRATION_BUTTON), "Registration form registration button is not presented"
        assert self.is_element_present(
            *RegistrationFormLocators.REGISTRATION_CLIENT_DOWNLOAD_LINK), "Registration form client dowload link is not presented"

    def switch_language(self, language):
        # открываем список языков
        assert self.is_element_present(
            *LandingPageLocators.LANDING_LANGUAGE_PICKER), "Language picker is not presented"
        language_picker = self.browser.find_element(*LandingPageLocators.LANDING_LANGUAGE_PICKER)
        language_picker.click()

        # меняем язык
        assert self.is_element_present(By.CSS_SELECTOR, "a.lang-picker__list-a.--" + language), "Language(" + language + ") is not in list"
        language_picker_language = self.browser.find_element(By.CSS_SELECTOR, "a.lang-picker__list-a.--" + language)
        language_picker_language.click()

        # проверяем что перешли на url с правильным языком
        assert "warthunder.com/" + language + '/test_task' in self.browser.current_url, "These aren't language(" + language + ") you're looking for."

        # открываем список языков
        assert self.is_element_present(
            *LandingPageLocators.LANDING_LANGUAGE_PICKER), "Language picker is not presented after change to " + language
        language_picker = self.browser.find_element(*LandingPageLocators.LANDING_LANGUAGE_PICKER)
        language_picker.click()

        # проверяем что сменилась иконка языка
        assert  self.is_element_present(By.CSS_SELECTOR, "div.lang-picker__current.--" + language), "Language picker(" + language + ") icon are not what they seem"

        # проверяем что язык на который мы перешли исчез из списка
        assert self.is_element_present(
            By.CSS_SELECTOR, "li.lang-picker__list-item.ng-scope.ng-hide > a.lang-picker__list-a.--" + language), "Language(" + language + ") is still in list"

    def go_to_login_page_from_registration_form(self, email):
        time.sleep(2)

        assert self.is_element_present(
            *RegistrationFormLocators.REGISTRATION_EMAIL_INPUT), "Registration form email input is not presented"
        email_input = self.browser.find_element(*RegistrationFormLocators.REGISTRATION_EMAIL_INPUT)
        email_input.send_keys(email)

        time.sleep(2)

        assert self.is_element_present(*RegistrationFormLocators.REGISTRATION_FORM_LOGIN_BUTTON), "Registration login button is not presented"
        login_button = self.browser.find_element(*RegistrationFormLocators.REGISTRATION_FORM_LOGIN_BUTTON)
        login_button.click()



