import re
from pathlib import Path

from playwright.sync_api import Locator, Page

import data
import locators
import pages
from config.project_path import PathManager
from data.assertions import Assertions


class ProductPage:
    def __init__(self):
        self.assertion = Assertions()
        self.path_manager = PathManager()
        self.uri_product: str = f"{data.host}inventory.html"
        self.file_format: str = ".png"
        self.base_format: str = self.path_manager.normalize_extension(self.file_format)
        self.timeout: int = 500

    def open_product_page(self, page: Page) -> Page:
        self.assertion.have_url(
            page, url=self.uri_product, msg="the url does not match"
        )
        self.assertion.have_url(page, self.uri_product, msg="the url does not match")

    def _click_btn_back_to_products(self, page: Page) -> None:
        pages.base_page.click(page, selector=locators.product.BACK_TO_PRODUCTS_BTN)

    def _get_elements_all_products(self, page: Page) -> Locator:
        return pages.base_page.get_elements(
            page, selector=locators.product.PROD_ITEMS_LIST
        )

    def _extract_path_screenshot(self) -> Path:
        return self.path_manager.extract_path(
            self.path_manager.create_dir("screenshots", "products_page")
        )

    def _get_sanitized_filename(self, text: str) -> str:
        """Очищает текст от недопустимых символов в именах файлов"""
        clean_text = re.sub(r'[\\/*?:"<>|]', "_", text.strip())
        return clean_text[:50]  # Ограничение длины имени файла

    def click_on_element_products(self, page: Page) -> None:
        screenshot_dir = self._extract_path_screenshot()
        elements = self._get_elements_all_products(page)

        for _, element in enumerate(elements):  # noqa
            element_text = element.text_content().strip()
            safe_name = self._get_sanitized_filename(element_text)
            element.click()
            page.wait_for_load_state("load", timeout=self.timeout)
            screenshot_path: Path = screenshot_dir / f"{safe_name}{self.base_format}"
            page.screenshot(path=screenshot_path, full_page=True)
            self._click_btn_back_to_products(page)

    def assert_visible_title_products(self, page: Page) -> None:
        self.assertion.is_visible(
            page, selector=locators.product.PRODUCTS_TITLE, msg="element is not visible"
        )
