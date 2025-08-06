import logging

import pytest
from playwright.sync_api import Page

import data
import pages

# Инициализируем логгер на уровне модуля
logger = logging.getLogger(__name__)


@pytest.mark.positive
@pytest.mark.usefixtures("user_login")
class TestMarketSorting:
    @pytest.mark.TC_006
    @pytest.mark.parametrize(
        ("sort_option", "expected_order"), data.data_for_tests.sorting_options
    )
    def test_product_sorting(self, page: Page, sort_option, expected_order):
        try:
            # Логируем начало теста
            logger.info(f"Starting sorting test: {sort_option}")
            logger.debug(f"Expected order: {expected_order}")

            # Выполняем тестовый сценарий
            pages.market_sorting.market_sorting_name_a_to_z(
                page, sort_opt=sort_option, expected_order=expected_order
            )

            # Логируем успешное завершение
            logger.info(f"Sorting test passed: {sort_option}")

        except Exception as e:
            # Логируем ошибку с полной информацией
            logger.error(f"Test failed: {sort_option}", exc_info=True)
            pytest.fail(f"Test failed: {e}")
