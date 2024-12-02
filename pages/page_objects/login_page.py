from playwright.sync_api import Page, expect

from pages.locators.login_page_locators import LoginPageLocators
from pages.page_objects.base_page import BasePage


class LoginPage(BasePage):
    URL = '/'

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.user_name_input = page.locator(LoginPageLocators.USER_NAME_INPUT)
        self.password_input = page.locator(LoginPageLocators.USER_PASSWORD_INPUT)
        self.submit_button = page.locator(LoginPageLocators.LOGIN_BUTTON)
        self.error_message = page.locator(LoginPageLocators.ERROR_MESSAGE)
        self.shopping_cart_icon = page.locator(LoginPageLocators.SHOPPING_CART_ICON)
        self.products_page_title = page.get_by_text('Products').first

    def login(self, user_data: dict) -> None:
        self.user_name_input.fill(user_data['username'])
        self.password_input.fill(user_data['password'])
        self.submit_button.click()

    def user_is_logged_in(self) -> None:
        expect(self.products_page_title).to_be_visible()
        expect(self.shopping_cart_icon).to_be_visible()

    def error_message_is_present(self, expected_error_message) -> None:
        expect(self.error_message).to_be_visible()
        expect(self.error_message).to_contain_text(expected_error_message)
