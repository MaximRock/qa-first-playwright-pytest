import pytest
import logging
from playwright.async_api import Page

import data
import pages

logger = logging.getLogger(__name__)


@pytest.mark.positive
@pytest.mark.usefixtures("user_login")
class TestBurgerMenuProductPage:

    @pytest.mark.TC_002
    @pytest.mark.smoke
    def test_open_and_close_burger_menu(self, page: Page):
        try:
            logger.info(
                f"Starting test: {self.__class__.__name__}.test_open_and_close_burger_menu"
            )

            pages.burger_menu_products_page.open_and_close_burger_menu(page)

            logger.info(
                f"Finished test: {self.__class__.__name__}.test_open_and_close_burger_menu"
            )
        except Exception as e:
            logger.error(
                f"Failed test: {self.__class__.__name__}.test_open_and_close_burger_menu",
                exc_info=True,
            )
            pytest.fail(
                f"Failed test: {self.__class__.__name__}.test_open_and_close_burger_menu, {e}"
            )

    @pytest.mark.TC_003
    @pytest.mark.parametrize("menu_buttons", data.data_for_tests.text_pruduct_menu)
    def test_compare_list_buttons_with_text(
        self, page: Page, menu_buttons: str
    ) -> None:
        try:
            logger.info(f"Starting text comparison test for button: {menu_buttons}")

            logger.debug(f"Getting elements from page: {page}")
            elements = pages.burger_menu_products_page.get_text_from_all_elements(page)
            data.assertion.check_text_in_list(elements, menu_buttons)

            logger.info(
                f"Text comparison successful for: {menu_buttons} | Elements: {elements}"
            )
        except Exception as e:
            logger.error(f"Test failed for button: {menu_buttons}", exc_info=True)
            logger.error(f"Expected: {menu_buttons} | Actual: {elements}")
            pytest.fail(f"Test failed for button: {menu_buttons}, {str(e)}")
