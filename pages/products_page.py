from playwright.sync_api import Page


class ProductsPage:
    def __init__(self, page: Page):
        self.page = page
        self.title_class = ".title"
        self.add_to_cart_buttons = "button[id*='add-to-cart']"
        self.shopping_cart_link = ".shopping_cart_link"
        self.product_name = ".inventory_item_name"

    def navigate(self):
        self.page.goto("https://www.saucedemo.com/inventory.html")

    def get_title(self):
        return self.page.text_content(self.title_class)

    def add_first_product_to_cart(self):
        self.page.click(f"{self.add_to_cart_buttons}:nth-of-type(1)")

    def go_to_cart(self):
        self.page.click(self.shopping_cart_link)

    def get_first_product_name(self):
        return self.page.text_content(f"{self.product_name}:nth-of-type(1)")
