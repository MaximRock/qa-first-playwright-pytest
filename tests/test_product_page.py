
from venv import logger
import pytest
import logging
from playwright.sync_api._generated import Page

import pages

logger = logging.getLogger(__name__)

@pytest.mark.positive
@pytest.mark.smoke
@pytest.mark.usefixtures("user_login")
class TestProductPage:

    def test_open_product_page(self, page: Page):
        test_name = f"{self.__class__.__name__}.test_open_product_page"

        try:
            logger.info(f"Start test: {test_name}")
            pages.product_page.open_product_page(page)
            logger.info(f"End test: {test_name}")
        except Exception as e:
            logger.error(f"Error test: {test_name}", exc_info=True)
            logger.error(f"Test error: {test_name} - {str(e)}")
            pytest.fail(f"Test error: {test_name} - {str(e)}")

    def test_click_all_elements_products(self, page: Page):
        test_name = f"{self.__class__.__name__}.test_click_all_elements_products"

        try:
            logger.info(f"Strart test: {test_name}")

            pages.product_page.click_on_element_products(page)
            pages.product_page.assert_visible_title_products(page)

            logger.info(f"End test: {test_name}")
        except AssertionError as e:
            logger.error(f"Error test: {test_name}", exc_info=True)
            logger.error(f"Test error: {test_name} - {str(e)}")
            pytest.fail(f"Test error: {test_name} - {str(e)}")

        # elements = page.locator(
        #     "//div[@class='inventory_item_description']/div/a"
        # ).all()
        # back = page.locator("//button[contains(text(), 'Back to products')]")
        # for element in elements:
        #     # page.wait_for_timeout(1000)
        #     print(element.text_content())
        #     element.click()
        #     back.click()


# //div[@class='pricebar']/button[contains(@class, 'inventory_item_price')]


# @pytest.mark.parametrize("menu_buttons",  data.data_for_tests.text_pruduct_menu)
# def test_click(self, page: Page, menu_buttons):
#     elements = pages.product_page.get_text_from_all_elements(page)

#     assert menu_buttons in elements
#     print(f"Testing: {menu_buttons} | {elements}")

# pages.product_page.assert_text_from_all_elements(page, menu_buttons)

# pages.product_page.click_burger_btn(page)
# buttons = page.locator(".bm-menu>.bm-item-list>a").all()
# print([i.text_content() for i in buttons])

#    def test_open_close_burger_menu(self, page: Page):
#        pages.product_page.click_close_burger_menu(page)
#        pages.product_page.visible_burger_menu_btn(page)

# def test_click_burger_btn(self, page: Page):
#     pages.product_page.click_burger_btn(page)
#     pages.product_page.visible_close_burger_menu(page)

#     pages.product_page.click_close_burger_menu(page)
#     pages.product_page.visible_burger_menu_btn(page)

# @pytest.mark.parametrize("menu_buttons", data.data_for_tests.text_pruduct_menu)
# def test_compare_list_buttons_with_text(
#     self, page: Page, menu_buttons: str
# ) -> None:
#     elements = pages.product_page.get_text_from_all_elements(page)
#     data.assertion.check_text_in_list(elements, menu_buttons)
#     print(f"Testing: {menu_buttons} | {elements}")
