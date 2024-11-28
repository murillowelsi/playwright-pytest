from pages.page_objects.main_page import MainPage
from pages.page_objects.products_page import ProductsPage


def test_valid_login(
    main_page: MainPage, products_page: ProductsPage, normal_user_data
):
    main_page.load()
    main_page.login(normal_user_data)
    products_page.user_is_logged_in()
