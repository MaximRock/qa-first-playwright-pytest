import os

import pytest
from playwright.sync_api import Page

import pages


@pytest.fixture(scope="class")
def user_login(page: Page):
    pages.login_page.auth_login_page(
        page, os.getenv("AUTH_LOGIN"), os.getenv("AUTH_PASSWORD")
    )
