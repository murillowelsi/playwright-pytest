from playwright.sync_api import Page, expect

from pages.locators.products_page_locators import ProductsPageLocators
from pages.page_objects.base_page import BasePage


class ProductsPage(BasePage):
    URL = '/inventory.html'

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.page_title = page.get_by_text(ProductsPageLocators.PAGE_TITLE)

    def user_is_logged_in(self) -> None:
        expect(self.page.get_by_text('Products').first).to_be_visible()
        expect(
            self.page.locator(ProductsPageLocators.SHOPPING_CART_ICON)
        ).to_be_visible()

    def user_is_not_logged_in(self) -> None:
        error_message = (
            'Epic sadface: Username and password do not match any user in this service'
        )

        expect(self.page.locator('[data-test="error"]')).to_be_visible()
        expect(self.page.locator('[data-test="error"]')).to_contain_text(error_message)
