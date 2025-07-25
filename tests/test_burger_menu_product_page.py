import pytest
from playwright.async_api import Page

import data
import pages


@pytest.mark.usefixtures("user_login")
class TestBurgerMenuProductPage:
    def test_open_and_close_burger_menu(self, page: Page):
        pages.burger_menu_products_page.click_burger_btn(page)
        pages.burger_menu_products_page.visible_close_burger_menu(page)

        pages.burger_menu_products_page.click_close_burger_menu(page)
        pages.burger_menu_products_page.visible_burger_menu_btn(page)

    @pytest.mark.parametrize("menu_buttons", data.data_for_tests.text_pruduct_menu)
    def test_compare_list_buttons_with_text(
        self, page: Page, menu_buttons: str
    ) -> None:
        elements = pages.burger_menu_products_page.get_text_from_all_elements(page)
        data.assertion.check_text_in_list(elements, menu_buttons)
        print(f"Testing: {menu_buttons} | {elements}")
