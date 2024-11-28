import pytest
from faker import Faker
from playwright.sync_api import Page

from pages.page_objects.main_page import MainPage
from pages.page_objects.products_page import ProductsPage


@pytest.fixture(scope='session')
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        'viewport': {
            'width': 1920,
            'height': 1080,
        },
    }


@pytest.fixture()
def main_page(page: Page):
    return MainPage(page)


@pytest.fixture()
def products_page(page: Page):
    return ProductsPage(page)


faker = Faker()


@pytest.fixture
def normal_user_data():
    return {
        'username': 'standard_user',
        'password': 'secret_sauce',
    }


@pytest.fixture
def invalid_user_data():
    return {
        'username': faker.name(),
        'password': faker.password(length=16),
    }
