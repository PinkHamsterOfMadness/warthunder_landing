from .pages.landing_page import LandingPage
from .pages.login_page import LoginPage
import pytest


@pytest.mark.parametrize('language', ["en", "de", "ru", "es", "fr", "pl", "pt", "tr", "cz", "zh"])
def test_guest_can_see_all_element_landing_page(browser, language):
    page = LandingPage(browser, "https://warthunder.com/" + language + "/test_task/")
    page.open()
    page.search_all_elements()
    if language == "ru":
        page.search_ru_customer_support_link()
    else:
        page.search_en_customer_support_link()
    page.open_registration_form()
    page.search_all_elements_registration_form()


@pytest.mark.parametrize('language_to', ["en", "de", "ru", "es", "fr", "pl", "pt", "tr", "cz", "zh"])
@pytest.mark.parametrize('language_from', ["en", "de", "ru", "es", "fr", "pl", "pt", "tr", "cz", "zh"])
def test_guest_can_change_language(browser, language_from, language_to):
    if language_from != language_to:
        page = LandingPage(browser, "https://warthunder.com/" + language_from + "/test_task/")
        page.open()
        page.switch_language(language_to)
        page.search_all_elements()
        if language_to == "ru":
            page.search_ru_customer_support_link()
        else:
            page.search_en_customer_support_link()
        page.open_registration_form()
        page.search_all_elements_registration_form()


@pytest.mark.parametrize('language', ["en", "de", "ru", "es", "fr", "pl", "pt", "tr", "cz", "zh"])
def test_user_can_login_from_registration_page(browser, language):
    page = LandingPage(browser, "https://warthunder.com/" + language + "/test_task/")
    page.open()
    page.open_registration_form()
    page.go_to_login_page_from_registration_form("k0syach0k@bk.ru")
    page = LoginPage(browser, browser.current_url)
    page.check_login_page(language)
    page.login("k0syach0k@bk.ru", "123456")
    page.check_account_page(language)




