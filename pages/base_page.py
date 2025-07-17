from playwright.sync_api import Page, Response, TimeoutError
import data



class BasePage:

    def open(self, page: Page) -> Page:
        page.goto(data.host)

    def input(self, page: Page, selector: str, text: str) -> None:
        page.locator(selector).fill(text)
