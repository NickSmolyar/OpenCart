from typing import Optional

import pytest
from playwright.sync_api import BrowserContext, Page

from config.urls import URLs
from tests.pages.base_component import BaseComponent


class LoginPage(BaseComponent):
    def __init__(
            self,
            context: BrowserContext,
            page: Page,
            request: Optional[pytest.FixtureRequest] = None
    ):
        super().__init__(context, page, request)
        self.url = URLs.LOGIN

        self.continue_button = page.locator("a.btn-primary:has-text('Continue')")
        self.email_input = page.locator("#input-email")
        self.password_input = page.locator("#input-password")
        self.login_button = page.locator("button.btn.btn-primary:has-text('Login')")
        self.logout_button = page.locator(".dropdown-menu .dropdown-item:has-text('Logout')")
        self.product_search_field = page.locator("input[placeholder='Search']")

    def open_login_page(self) -> None:
        self.page.goto(self.url)

    def fill_form(self, email: str, password: str) -> None:
        self.email_input.fill(email)
        self.password_input.fill(password)

    def submit_login(self) -> None:
        self.login_button.click()

    def type_and_search(self, query: str) -> None:
        self.product_search_field.fill(query)
        self.product_search_field.press("Enter")
