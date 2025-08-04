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

        for _, element in enumerate(elements):
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

        # for index, element in enumerate(elements):
        #     try:
        #         # Кликаем на элемент
        #         element.click()
        #         page.wait_for_timeout(300)

        #         # Формируем корректное имя файла
        #         screenshot_path = screenshot_dir / f"product_{index}.png"

        #         # Делаем скриншот
        #         page.screenshot(
        #             path=str(screenshot_path),  # Явное преобразование Path в строку
        #             full_page=True,
        #         )

        #         # Возвращаемся назад
        #         self._click_btn_back_to_products(page)

        #     except Exception as e:
        #         print(f"Ошибка при сохранении скриншота для элемента {index}: {e}")

        # for element in self.get_text_from_all_elements(page):
        # assert (element in lst), ()

        # def _screen_product_list(self, page: Page) -> None:

    #     path_screen = self._create_dir_screenshot() / f'{}.png'
    #     pages.base_page.page_screenshot(page, path='')

    # def click_burger_btn(self, page: Page) -> None:
    #     pages.base_page.click(page, selector=locators.product.PRODUCTS_BURGER_MENU_BTN)

    # def visible_close_burger_menu(self, page: Page) -> None:
    #     self.assertion.is_visible(
    #         page,
    #         selector=locators.product.PRODUCTS_CLOSE_BURGER_MENU_BTN,
    #         msg="the element is not visible",
    #     )

    # def click_close_burger_menu(self, page: Page) -> None:
    #     pages.base_page.click(
    #         page, selector=locators.product.PRODUCTS_CLOSE_BURGER_MENU_BTN
    #     )

    # def visible_burger_menu_btn(self, page: Page) -> None:
    #     self.assertion.is_visible(
    #         page,
    #         selector=locators.product.PRODUCTS_BURGER_MENU_BTN,
    #         msg="the element is not visible",
    #     )

    # def get_text_from_all_elements(self, page: Page) -> list:
    #     return pages.base_page.get_element_text(page, locators.product.PRODUCTS_MENU)

    # def assert_text_from_all_elements(self, lst: list, text: list) -> None:
    #     self.assertion.check_text_in_list(self, lst, text)
