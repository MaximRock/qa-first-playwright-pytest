import pytest
from playwright.async_api import Page

import pages


@pytest.mark.positive
@pytest.mark.smoke
@pytest.mark.usefixtures("user_login")
class TestCheckBadgeAddToCart:
    def test_check_badge_add_to_cart(self, page: Page):
        pages.market_product.add_to_cart(page)