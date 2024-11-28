from playwright.sync_api import Page, expect

from pages.locators.base_page_locators import BasePageLocators


class BasePage:
    URL: str

    def __init__(self, page: Page) -> None:
        self.page = page
        self.banner_title = page.get_by_text(BasePageLocators.BANNER_TITLE)

    def load(self) -> None:
        expected_banner = 'Swag Labs'
        self.page.goto(self.URL)
        expect(self.banner_title).to_contain_text(expected_banner)
