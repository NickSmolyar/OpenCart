from typing import Optional

import pytest
from playwright.sync_api import BrowserContext, Page

from OpenCart.opencart_docker.config.urls import LOGIN_URL
from OpenCart.opencart_docker.tests.pages.base_page import BaseComponent


class LoginPage(BaseComponent):
    def __init__(
            self,
            context: 'BrowserContext',
            page: 'Page',
            rel_url: str = '',
            full_url: str = LOGIN_URL,
            url_parameters: Optional[str] = None,
            request: Optional['pytest.FixtureRequest'] = None
    ):
        super().__init__(context, page, request)
        self.rel_url = rel_url
        self._full_url = full_url or ""
        self._url_parameters = url_parameters

        self.continue_button = page.locator("a.btn-primary:has-text('Continue')")
        self.email_input = "#input-email"
        self.password_input = "#input-password"
        self.login_button = page.locator("button.btn.btn-primary", has_text="Login")
        self.logout_button = page.locator(".dropdown-menu .dropdown-item", has_text="Logout")

    def navigate_to_login(self) -> None:
         self.page.goto(self._full_url or self.rel_url)

    def fill_form(self, email: str, password: str) -> None:
        self.page.fill(self.email_input, email)
        self.page.fill(self.password_input, password)




