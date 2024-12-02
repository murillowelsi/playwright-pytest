from pages.page_objects.login_page import LoginPage


def test_valid_login(login_page: LoginPage, normal_user_data):
    login_page.load()
    login_page.login(normal_user_data)
    login_page.user_is_logged_in()


def test_invalid_login(login_page: LoginPage, invalid_user_data):
    EXPECTED_MESSAGE = (
        'Epic sadface: Username and password do not match any user in this service'
    )
    login_page.load()
    login_page.login(invalid_user_data)
    login_page.error_message_is_present(EXPECTED_MESSAGE)


def test_locked_out_user_login(login_page: LoginPage, locked_out_user_data):
    EXPECTED_MESSAGE = 'Epic sadface: Sorry, this user has been locked out.'
    login_page.load()
    login_page.login(locked_out_user_data)
    login_page.error_message_is_present(EXPECTED_MESSAGE)
