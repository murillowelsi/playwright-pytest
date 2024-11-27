from playwright.sync_api import expect

from pages.page_objects.main_page import MainPage


def test_main_banner(main_page: MainPage) -> None:
    expected_banner = 'Playwright'
    expected_banner_subtitle = (
        'enables reliable end-to-end testing for modern web apps.'
    )

    main_page.load()

    expect(main_page.banner_title).to_contain_text(expected_banner)
    expect(main_page.banner_subtitle).to_contain_text(expected_banner_subtitle)


def test_get_started_link(main_page: MainPage) -> None:
    main_page.load()

    main_page.click_link()

    expect(main_page.heading).to_be_visible()
