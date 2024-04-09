from playwright.sync_api import sync_playwright
import pytest
from pages.login_page import LoginPage
from settings import USERNAME, PASSWORD


@pytest.fixture
def login_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        login_page = LoginPage(page)
        yield login_page
        browser.close()


def test_login_success(login_page):
    login_page.navigate()
    login_page.login(USERNAME, PASSWORD)
    assert login_page.page.url == "https://www.saucedemo.com/inventory.html"
