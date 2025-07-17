from email.mime import audio
from playwright.sync_api import Page
import pages

from locators.auth import Auth

class LoginPage:
    def __init__(self):
        self.auth = Auth()

    def open_login_page(self, page: Page):
        pages.base_page.open(page)
        # page.goto(config.url.DOMAIN_SHOT)

    def input_login_username(self, page: Page):
        pages.base_page.input(page, selector=self.auth.USERNAME_INPUT, text='standard_user')


    