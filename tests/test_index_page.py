import pytest
import pages

class TestFooter:

    def test_open_pages(self, page):
        pages.login_page.open_login_page(page)
        pages.login_page.input_login_username(page)