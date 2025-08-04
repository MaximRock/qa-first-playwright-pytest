import pytest
import logging
from playwright.async_api import Page

import pages

logger = logging.getLogger(__name__)

@pytest.mark.positive
@pytest.mark.smoke
@pytest.mark.usefixtures("user_login")
class TestCheckBadgeAddToCart:

    @pytest.mark.TC_007
    @pytest.mark.positive
    def test_check_badge_add_to_cart(self, page: Page):
        test_name = f"{self.__class__.__name__}.test_check_badge_add_to_cart"
        try:
            logger.info(f"Start test: {test_name}")
            pages.market_product.add_to_cart(page)
            logger.info(f"End test: {test_name}")
        except Exception as e:
            logger.error(f"Error test: {test_name}", exc_info=True)
            logger.error(f"Test error: {test_name} - {str(e)}")
            pytest.fail(f"Test error: {test_name} - {str(e)}")
