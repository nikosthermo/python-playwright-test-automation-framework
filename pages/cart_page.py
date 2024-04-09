from playwright.sync_api import Page


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_item = ".cart_item"
        self.checkout_button = "#checkout"

    def get_cart_items_count(self):
        return len(self.page.query_selector_all(self.cart_item))

    def checkout(self):
        self.page.click(self.checkout_button)

    def item_name(self, index=1):
        selector = f"{self.cart_item}:nth-of-type({index}) .inventory_item_name"
        self.page.wait_for_selector(selector, state="visible", timeout=60000)  # Wait for the element to be visible
        return self.page.text_content(selector)
