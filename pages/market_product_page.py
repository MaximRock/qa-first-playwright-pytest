from playwright.sync_api import Page

import pages
import locators
from data.assertions import Assertions

class MarketProductPage:
    def __init__(self):
        self.assertion = Assertions()

    def add_to_cart(self, page: Page):
        pages.base_page.click_by_element_index(page, selector=locators.product.PROD_ITEMS_LIST, index=0)
        pages.base_page.click(page, selector=locators.product.PROD_ITEM_ADD_TO_CART)

        self.assertion.is_visible(page, selector=locators.product.PRODUCTS_CART_BADGE, msg="Element is not visible")

