import pytest
from playwright.sync_api import expect

from data.login_data import LoginData
from helper.browser_manager import BrowserManager
from helper.csv_parser import CsvParser
from helper.utils import path_from_project_root
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

from playwright.sync_api import Playwright

csv_data = CsvParser(path_from_project_root('resources/test_data/login.csv'), LoginData)


def page_init(playwright: Playwright):
    return BrowserManager.initialize(playwright).new_page(ignore_https_errors=True)


@pytest.mark.parametrize('test_data', csv_data.filter_on_test_case_id('TC-1'))
def test_correct_username_and_correct_password(playwright: Playwright, test_data: LoginData):
    page = page_init(playwright)
    login_page = LoginPage(page)
    products_page = ProductsPage(page)

    login_page.goto().enter_username(test_data.username).enter_password(test_data.password).click_login()
    expect(products_page.fetch_section_title_locator()).to_have_text('Products')


@pytest.mark.parametrize('test_data', csv_data.filter_on_test_case_id('TC-2'))
def test_incorrect_username_and_correct_password(playwright: Playwright, test_data: LoginData):
    page = page_init(playwright)
    login_page = LoginPage(page)

    login_page.goto().enter_username(test_data.username).enter_password(test_data.password).click_login()
    expect(login_page.fetch_error_message_locator()).to_have_text(test_data.error_message)


@pytest.mark.parametrize('test_data', csv_data.filter_on_test_case_id('TC-3'))
def test_correct_username_and_incorrect_password(playwright: Playwright, test_data: LoginData):
    page = page_init(playwright)
    login_page = LoginPage(page)

    login_page.goto().enter_username(test_data.username).enter_password(test_data.password).click_login()
    expect(login_page.fetch_error_message_locator()).to_have_text(test_data.error_message)


@pytest.mark.parametrize('test_data', csv_data.filter_on_test_case_id('TC-4'))
def test_incorrect_username_and_incorrect_password(playwright: Playwright, test_data: LoginData):
    page = page_init(playwright)
    login_page = LoginPage(page)

    login_page.goto().enter_username(test_data.username).enter_password(test_data.password).click_login()
    expect(login_page.fetch_error_message_locator()).to_have_text(test_data.error_message)


@pytest.mark.parametrize('test_data', csv_data.filter_on_test_case_id('TC-5'))
def test_blank_username(playwright: Playwright, test_data: LoginData):
    page = page_init(playwright)
    login_page = LoginPage(page)

    login_page.goto().enter_username(test_data.username).enter_password(test_data.password).click_login()
    expect(login_page.fetch_error_message_locator()).to_have_text(test_data.error_message)


@pytest.mark.parametrize('test_data', csv_data.filter_on_test_case_id('TC-6'))
def test_blank_password(playwright: Playwright, test_data: LoginData):
    page = page_init(playwright)
    login_page = LoginPage(page)

    login_page.goto().enter_username(test_data.username).enter_password(test_data.password).click_login()
    expect(login_page.fetch_error_message_locator()).to_have_text(test_data.error_message)


@pytest.mark.parametrize('test_data', csv_data.filter_on_test_case_id('TC-7'))
def test_locked_out_user(playwright: Playwright, test_data: LoginData):
    page = page_init(playwright)
    login_page = LoginPage(page)

    login_page.goto().enter_username(test_data.username).enter_password(test_data.password).click_login()
    expect(login_page.fetch_error_message_locator()).to_have_text(test_data.error_message)
