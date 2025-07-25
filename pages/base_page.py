from playwright.sync_api import Locator, Page, ElementHandle, Response, TimeoutError
from typing import List

import data


class BasePage:
    def open(self, page: Page) -> Page:
        page.goto(data.host)

    def input(self, page: Page, selector: str, text: str) -> None:
        page.locator(selector).fill(text)

    def click(self, page: Page, selector: str) -> None:
        page.click(selector)

    def get_elements(self, page: Page, selector: str) -> List[ElementHandle]:
        return page.locator(selector).all()

    def get_element_text(self, page: Page, selector: str) -> list[str]:
        elements: Locator = page.locator(selector).all()
        return str([element.text_content() for element in elements])
    
    def click_by_text(self, page: Page, text: str) -> None:
        page.get_by_text(text).click()

    def page_screenshot(self, page: Page, path: str) -> None:
        page.screenshot(path, full_page=True)

