from playwright.async_api import Page

import locators
import pages
from data.assertions import Assertions

# loggger = logging.getLogger(__name__)

class MarketSorting:

    def __init__(self) -> None:
        self.assertion = Assertions()

    def market_sorting_name_a_to_z(
        self, page: Page, sort_opt: str, expected_order: list
    ) -> None:

        pages.base_page.dropdown_select(page, selector=locators.product.PROD_DROPDOWN_SELECT, value=sort_opt)
        actual_order = pages.base_page.get_element_text(
            page, selector=locators.product.PROD_ITEMS_LIST
        )
        page.wait_for_selector(locators.product.PROD_ITEMS_LIST)

        self.assertion.check_equals(expected=expected_order, actual=actual_order)

