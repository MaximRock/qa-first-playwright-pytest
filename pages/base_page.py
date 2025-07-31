from playwright.sync_api import (ElementHandle, Locator, Page, Response,
                                 TimeoutError)

import data


class BasePage:
    def open(self, page: Page) -> Page:
        page.goto(data.host)

    def input(self, page: Page, selector: str, text: str) -> None:
        page.locator(selector).fill(text)

    def click(self, page: Page, selector: str) -> None:
        page.click(selector)

    def get_elements(self, page: Page, selector: str) -> list[ElementHandle]:
        return page.locator(selector).all()

    def get_element_text(self, page: Page, selector: str) -> list[str]:
        elements: Locator = page.locator(selector).all()
        return [element.text_content() for element in elements]

    def click_by_text(self, page: Page, text: str) -> None:
        page.get_by_text(text).click()

    def page_screenshot(self, page: Page, path: str) -> None:
        page.screenshot(path, full_page=True)

    def click_by_element_index(self, page: Page, selector: str, index: int) -> None:
        page.locator(selector).nth(index).click()

    def dropdown_select(self, page: Page, selector: str, value: str) -> None:
        page.locator(selector).select_option(value)

