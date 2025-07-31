from playwright.sync_api import Page, expect
from playwright.sync_api._generated import Locator


class Assertions:
    # def __init__(self):
    #     self.page = Page()
    #     self.loc = self.page.locator()

    def have_text(self, page: Page, selector: str, text: str, msg: str):
        loc: Locator = page.locator(selector)
        expect(loc).to_have_text(text), msg

    def have_url(self, page: Page, url: str, msg: str):
        expect(page).to_have_url(url, timeout=1000), msg

    def partial_text(self, page: Page, selector: str, text: str, msg: str):
        loc: Locator = page.locator(selector)
        expect(loc).to_contain_text(text), msg

    def contains_class(self, page: Page, selector: str, class_name: str, msg: str):
        loc: Locator = page.locator(selector)
        expect(loc).to_contain_class(class_name), msg

    def is_visible(self, page: Page, selector: str, msg: str):
        loc: Locator = page.locator(selector)
        expect(loc).to_be_visible(visible=True), msg

    def check_text_in_list(self, actual, expected):
        assert expected in actual

    def check_equals(self, actual: list, expected: list):
        assert expected == actual
