import os

from playwright.sync_api import Page

import locators
import pages

from data.assertions import Assertions
from data.parametr_pairs import ParametrPairs
# from locators.auth import Auth
# from locators.products import Products


class LoginPage:
    def __init__(self):
        #       self.auth = Auth()
        #       self.product = Products()
        self.assertion = Assertions()
        self.auth_login = os.getenv("AUTH_LOGIN")
        self.auth_password = os.getenv("AUTH_PASSWORD")
        if self.auth_login and self.auth_password is None:
            raise ValueError(
                "Please set the environment variables AUTH_LOGIN and AUTH_PASSWORD"
            )
        self.pairs = ParametrPairs()

    def _open_login_page(self, page: Page) -> None:
        pages.base_page.open(page)
        # page.goto(config.url.DOMAIN_SHOT)

    def _input_login_username(self, page: Page, username_text) -> None:
        pages.base_page.input(
            page,
            selector=locators.auth.USERNAME_INPUT,
            text=username_text,  # text=self.auth_login
        )

    def _input_login_password(self, page: Page, password_text) -> None:
        pages.base_page.input(
            page,
            selector=locators.auth.PASSWORD_INPUT,
            text=password_text,  # text=self.auth_password
        )

    def _click_login_button(self, page: Page) -> None:
        pages.base_page.click(page, selector=locators.auth.LOGIN_BTN)

    def verify_login_success(self, page: Page) -> None:
        self.assertion.have_text(
            page,
            selector=locators.product.PRODUCTS_TITLE,
            text="Products",
            msg="the text does not match",
        )

    def verify_login_error(self, page: Page, text_error: str, msg_error: str) -> None:
        self.assertion.have_text(
            page, selector=locators.auth.LOGIN_ERROR_TEXT, text=text_error, msg=msg_error
        )

    def verify_error_text(self, page: Page) -> None:
        self.assertion.is_visible(
            page, locators.auth.LOGIN_ERROR, msg="error text is not visible"
        )

    def auth_login_page(self, page: Page, username: str, password: str) -> None:
        self._open_login_page(page)
        self._input_login_username(page, username_text=username)
        self._input_login_password(page, password_text=password)
        self._click_login_button(page)

    def empty_fields_login_page(self, page: Page) -> None:
        self._open_login_page(page)
        self._click_login_button(page)

    # def testdata(self) -> list[tuple[Any, ...]]:
    #     return [
    #         tuple(combination)
    #         for combination in AllPairs(
    #             self.pairs.parametr(self.auth_login, self.auth_password),
    #             filter_func=(
    #                 lambda row: not (
    #                     self.auth_login in row and self.auth_password in row
    #                 )
    #             ),
    #         )
    #     ]

    # def verify_error_text(self, page: Page, text: str, msg: str) -> None:
    #     self.assertion.partial_text(page, selector=self.auth.LOGIN_ERROR, text=text, msg=msg)
