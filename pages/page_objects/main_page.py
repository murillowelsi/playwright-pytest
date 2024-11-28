from playwright.sync_api import Page

from pages.locators.main_page_locators import MainPageLocators
from pages.page_objects.base_page import BasePage


class MainPage(BasePage):
    URL = '/'

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.user_name_input = page.locator(MainPageLocators.USER_NAME_INPUT)
        self.password_input = page.locator(MainPageLocators.USER_PASSWORD_INPUT)
        self.submit_button = page.locator(MainPageLocators.LOGIN_BUTTON)

    def login(self, user_data: dict) -> None:
        self.user_name_input.fill(
            user_data['username']
        )  # Correctly access the dictionary
        self.password_input.fill(user_data['password'])
        self.submit_button.click()
