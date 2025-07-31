import pytest
import logging
from playwright.sync_api import Page

import pages
import data

# Инициализируем логгер на уровне модуля
logger = logging.getLogger(__name__)


@pytest.mark.positive
@pytest.mark.usefixtures("user_login")
class TestMarketSorting:

    @pytest.mark.parametrize(
        "sort_option, expected_order", data.data_for_tests.SORTING_OPTIONS
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

    # def test_sort(self, page: Page):
    #     page.locator(locators.product.PROD_DROPDOWN_SELECT).select_option(value="lohi")
    #     elements = page.locator(locators.product.PROD_ITEMS_LIST).all()

    #     for el in elements:
    #         print(el.text_content())

    # # Применяем сортировку
    # page.locator("//select[@class='product_sort_container']").select_option(
    #     value=sort_option
    # )

    # # Ждем применения сортировки (опционально)
    # page.wait_for_timeout(500)  # Краткая задержка для стабилизации

    # # Получаем все элементы продуктов
    # product_elements = page.locator(locators.product.PROD_ITEMS_LIST).all()

    # # Проверяем количество элементов
    # assert len(product_elements) == len(
    #     expected_order
    # ), f"Expected {len(expected_order)} products, found {len(product_elements)}"

    # # Извлекаем названия продуктов
    # actual_order = [element.text_content() for element in product_elements]

    # # Сравниваем фактический и ожидаемый порядок
    # assert (
    #     actual_order == expected_order
    # ), f"Sorting {sort_option} failed.\nExpected: {expected_order}\nActual: {actual_order}"
