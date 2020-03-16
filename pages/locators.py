from selenium.webdriver.common.by import By


class LandingPageLocators():
    LANDING_LANGUAGE_PICKER = (By.CSS_SELECTOR, "div.lang-picker")
    LANDING_LANGUAGE_PICKER_EN = (By.CSS_SELECTOR, "a.lang-picker__list-a.--en")
    LANDING_LANGUAGE_PICKER_DE = (By.CSS_SELECTOR, "a.lang-picker__list-a.--de")
    LANDING_LANGUAGE_PICKER_RU = (By.CSS_SELECTOR, "a.lang-picker__list-a.--ru")
    LANDING_LANGUAGE_PICKER_ES = (By.CSS_SELECTOR, "a.lang-picker__list-a.--es")
    LANDING_LANGUAGE_PICKER_FR = (By.CSS_SELECTOR, "a.lang-picker__list-a.--fr")
    LANDING_LANGUAGE_PICKER_PL = (By.CSS_SELECTOR, "a.lang-picker__list-a.--pl")
    LANDING_LANGUAGE_PICKER_PT = (By.CSS_SELECTOR, "a.lang-picker__list-a.--pt")
    LANDING_LANGUAGE_PICKER_TR = (By.CSS_SELECTOR, "a.lang-picker__list-a.--tr")
    LANDING_LANGUAGE_PICKER_CZ = (By.CSS_SELECTOR, "a.lang-picker__list-a.--cz")
    LANDING_LANGUAGE_PICKER_ZH = (By.CSS_SELECTOR, "a.lang-picker__list-a.--zh")

    LANDING_LOGO = (By.CSS_SELECTOR, "img.landml__logo-img")
    LANDING_SPECIAL_LOGO = (By.CSS_SELECTOR, "img.special-logo__image")
    LANDING_REGISTRATION_BUTON = (By.CSS_SELECTOR, "a.landing__register-btn")

    LANDING_FOOTER_GAIJIN_LOGO = (By.CSS_SELECTOR, "i.footer__image.--gaijin")
    LANDING_FOOTER_PC_LOGO = (By.CSS_SELECTOR, "div.footer__image.--pc")
    LANDING_FOOTER_MAC_LOGO = (By.CSS_SELECTOR, "div.footer__image.--mac")
    LANDING_FOOTER_PS4_LOGO = (By.CSS_SELECTOR, "div.footer__image.--ps4")
    LANDING_FOOTER_GAMESCOM = (By.CSS_SELECTOR, "div.footer__image.--gamescom")
    LANDING_FOOTER_PEGI = (By.CSS_SELECTOR, "i.footer__image.--pegi")

    LANDING_PRIVACY_POLICY_LINK = (By.CSS_SELECTOR, "div.footer__links > div:nth-child(1) > a")
    LANDING_EULA_LINK = (By.CSS_SELECTOR, "div.footer__links > div:nth-child(2) > a")
    LANDING_TERMS_OF_USE_LINK = (By.CSS_SELECTOR, "div.footer__links > div:nth-child(3) > a")
    LANDING_CUSTOMER_SUPPORT_EN_LINK = (By.CSS_SELECTOR, "div.footer__links > div:nth-child(4) > a:nth-child(2)")
    LANDING_CUSTOMER_SUPPORT_RU_LINK = (By.CSS_SELECTOR, "div.footer__links > div:nth-child(4) > a:nth-child(1)")


class RegistrationFormLocators():
    REGISTRATION_FORM = (By.CSS_SELECTOR, "div.registration")
    REGISTRATION_FORM_EXIT = (By.CSS_SELECTOR, "a.registration__close")

    REGISTRATION_FORM_LOGIN_BUTTON = (By.CSS_SELECTOR, "a.registration__email-busy-button.--red")
    REGISTRATION_FORM_RECOVER_PASSWORD_BUTTON = (By.CSS_SELECTOR, "a.registration__email-busy-button.--green")
    REGISTRATION_EMAIL_INPUT = (By.CSS_SELECTOR, "#emailInput")
    REGISTRATION_NICKNAME_INPUT = (By.CSS_SELECTOR, "#nicknameInput")
    REGISTRATION_PASSWORD_INPUT = (By.CSS_SELECTOR, "#passwordInput")
    REGISTRATION_PASSWORD_REPEAT_INPUT = (By.CSS_SELECTOR, "#passwordRepeatInput")
    REGISTRATION_CAPTCHA_INPUT = (By.CSS_SELECTOR, "#captchaInput")
    REGISTRATION_CAPTCHA_RELOAD = (By.CSS_SELECTOR, "a.captcha__reload")
    REGISTRATION_CAPTCHA_IMAGE = (By.CSS_SELECTOR, "#captcha")
    REGISTRATION_EULA_CHECKBOX = (By.CSS_SELECTOR, "#eulaInput")
    REGISTRATION_EULA_LINK = (By.CSS_SELECTOR, "label.checkbox__label > div > a:nth-child(1)")
    REGISTRATION_TERMS_OF_USE_LINK = (By.CSS_SELECTOR, "label.checkbox__label > div > a:nth-child(2)")
    REGISTRATION_PRIVACY_POLICY_LINK = (By.CSS_SELECTOR, "label.checkbox__label > div > a:nth-child(3)")
    REGISTRATION_SUBSCRIBE_CHECKBOX = (By.CSS_SELECTOR, "#subscribeInput")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "input.form-input__submit.btn-wt")
    REGISTRATION_CLIENT_DOWNLOAD_LINK = (By.CSS_SELECTOR, "a.registration__download-link")


class LoginPageLocators():
    LOGIN_EMAIL_INPUT = (By.CSS_SELECTOR, "#email")
    LOGIN_PASSWORD_INPUT = (By.CSS_SELECTOR, "#password")
    LOGIN_AUTHORIZATION_BUTTON = (By.CSS_SELECTOR, ".submit.btn")
    LOGIN_REGISTRATION_LINK = (By.CSS_SELECTOR, "div.create.xs-center > a")
    LOGIN_CHOOSE_ACCOUNT_LINK = (By.CSS_SELECTOR, "a.list-group-item.auth-link.auth-link--caret")
