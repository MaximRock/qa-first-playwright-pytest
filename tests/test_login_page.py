import pytest
import os

import pages
import data


class TestLoginPage:

    def test_auth_login_page(self, page):
        pages.login_page.auth_login_page(page, os.getenv("AUTH_LOGIN"), os.getenv("AUTH_PASSWORD"))
        pages.login_page.verify_login_success(page)

    def test_empty_fields_login_page(self, page):
        pages.login_page.empty_fields_login_page(page)
        pages.login_page.verify_login_error(
            page,
            text_error="Epic sadface: Username is required",
            msg_error="the text does not match",
        )

    @pytest.mark.parametrize(
        "username, password",
        data.testdata,
        ids=[f"{i+1}" for i in range(len(data.testdata))],
    )
    def test_error_pairs(self, page, username, password):
        pages.login_page.auth_login_page(page, username, password)
        pages.login_page.verify_error_text(page)
        print(f"\nTesting: {username} | {password}")

