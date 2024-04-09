# tests/test_products_page.py
import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from settings import USERNAME, PASSWORD


@pytest.fixture
def products_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login(USERNAME, PASSWORD)
        products_page = ProductsPage(page)
        yield products_page
        browser.close()


def test_products_page_title(products_page):
    products_page.navigate()
    assert "Products" in products_page.get_title(), "Title does not match."


def test_add_first_product_to_cart_and_verify(products_page):
    products_page.navigate()
    products_page.add_first_product_to_cart()
    products_page.go_to_cart()
    cart_page = CartPage(products_page.page)
    assert cart_page.get_cart_items_count() == 1, "Cart should have 1 item."
    first_product_name = products_page.get_first_product_name()
    assert first_product_name == "Sauce Labs Backpack", "Added product name does not match the first product."
