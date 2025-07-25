from playwright.sync_api import Page

import locators
import pages
from data.assertions import Assertions


class BurgerMenuProductsPage:
    def __init__(self) -> None:
        self.assertion = Assertions()

    def click_burger_btn(self, page: Page) -> None:
        pages.base_page.click(page, selector=locators.product.PRODUCTS_BURGER_MENU_BTN)

    def visible_close_burger_menu(self, page: Page) -> None:
        self.assertion.is_visible(
            page,
            selector=locators.product.PRODUCTS_CLOSE_BURGER_MENU_BTN,
            msg="the element is not visible",
        )

    def click_close_burger_menu(self, page: Page) -> None:
        pages.base_page.click(
            page, selector=locators.product.PRODUCTS_CLOSE_BURGER_MENU_BTN
        )

    def visible_burger_menu_btn(self, page: Page) -> None:
        self.assertion.is_visible(
            page,
            selector=locators.product.PRODUCTS_BURGER_MENU_BTN,
            msg="the element is not visible",
        )

    def get_text_from_all_elements(self, page: Page) -> list:
        return pages.base_page.get_element_text(page, locators.product.PRODUCTS_MENU)

    def assert_text_from_all_elements(self, lst: list, text: list) -> None:
        self.assertion.check_text_in_list(self, lst, text)
