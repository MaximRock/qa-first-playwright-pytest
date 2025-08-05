import logging

import pytest
from playwright.sync_api._generated import Page

import pages

logger = logging.getLogger(__name__)


@pytest.mark.positive
@pytest.mark.smoke
@pytest.mark.usefixtures("user_login")
class TestProductPage:
    @pytest.mark.TC_004
    def test_open_product_page(self, page: Page):
        test_name = f"{self.__class__.__name__}.test_open_product_page"

        try:
            logger.info(f"Start test: {test_name}")

            pages.product_page.open_product_page(page)

            logger.info(f"End test: {test_name}")
        except Exception as e:
            logger.error(f"Error test: {test_name}", exc_info=True)
            logger.error(f"Test error: {test_name} - {e!s}")
            pytest.fail(f"Test error: {test_name} - {e!s}")

    @pytest.mark.TC_005
    def test_click_all_elements_products(self, page: Page):
        test_name = f"{self.__class__.__name__}.test_click_all_elements_products"

        try:
            logger.info(f"Strart test: {test_name}")

            pages.product_page.click_on_element_products(page)
            pages.product_page.assert_visible_title_products(page)

            logger.info(f"End test: {test_name}")
        except AssertionError as e:
            logger.error(f"Error test: {test_name}", exc_info=True)
            logger.error(f"Test error: {test_name} - {e!s}")
            pytest.fail(f"Test error: {test_name} - {e!s}")
