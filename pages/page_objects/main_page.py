from playwright.sync_api import Page

from pages.locators.main_page_locators import MainPageLocators
from pages.page_objects.base_page import BasePage


class MainPage(BasePage):
    URL = '/'

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.banner_title = page.locator(MainPageLocators.BANNER_TITLE)
        self.banner_subtitle = page.locator(MainPageLocators.BANNER_SUBTITLE)
        self.link = page.get_by_role('link', name=MainPageLocators.LINK)
        self.heading = page.get_by_role('heading', name=MainPageLocators.HEADING)

    def click_link(self) -> None:
        self.link.click()
