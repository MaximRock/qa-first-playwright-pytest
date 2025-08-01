import pytest
import os
import logging

import pages
import data


logger = logging.getLogger(__name__)


class TestLoginPage:

    @pytest.mark.TC_001
    @pytest.mark.positive
    @pytest.mark.smoke
    def test_auth_login_page(self, page):
        test_name = f"{self.__class__.__name__}.test_auth_login_page"
        try:
            logger.info(f"Test auth login page: {test_name}")
            logger.debug(
                f'Get username: {os.getenv("AUTH_LOGIN")} and password: {os.getenv("AUTH_PASSWORD")}'
            )
            logger.info("Attempting user authentication")
            pages.login_page.auth_login_page(
                page, os.getenv("AUTH_LOGIN"), os.getenv("AUTH_PASSWORD")
            )
            pages.login_page.verify_login_success(page)
            logger.info(f"Test passed: {test_name}")
        except Exception as e:
            logger.error(f"Test failed: {test_name}", exc_info=True)
            logger.error(
                f"Authentication details - username: {os.getenv("AUTH_LOGIN")}"
            )
            logger.error(f"Error details: {str(e)}")
            pytest.fail(f"Test failed: {test_name} - {str(e)}")

    @pytest.mark.negative
    @pytest.mark.smoke
    def test_empty_fields_login_page(self, page):
        test_name = f"{self.__class__.__name__}.test_empty_fields_login_page"
        try:
            logger.info(f"Test empty fields login page: {test_name}")
            pages.login_page.empty_fields_login_page(page)

            pages.login_page.verify_login_error(
                page,
                text_error="Epic sadface: Username is required",
                msg_error="the text does not match",
            )
            logger.info(f"Test passed: {test_name}")
        except Exception as e:
            logger.error(f"Test failed: {test_name}", exc_info=True)
            logger.error(f"Error details: {str(e)}")
            pytest.fail(f"Test failed: {test_name} - {str(e)}")

    @pytest.mark.negative
    @pytest.mark.parametrize(
        "username, password",
        data.testdata,
        ids=[f"{i+1}" for i in range(len(data.testdata))],
    )
    def test_error_pairs(self, page, username, password):
        test_name = f"{self.__class__.__name__}.test_error_pairs"
        try:
            logger.info(f"Test error pairs: {test_name}")
            pages.login_page.auth_login_page(page, username, password)
            pages.login_page.verify_error_text(page)
            logger.info(f"Test passed: {test_name}")
            logger.debug(f"Test: {username} | {password}")
        except Exception as e:
            logger.error(f"Test failed: {test_name}", exc_info=True)
            logger.error(f"Error details: {str(e)}")
            pytest.fail(f"Test failed: {test_name} - {str(e)}")
