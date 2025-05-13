from typing import Optional

import pytest
from playwright.sync_api import BrowserContext, Page

from OpenCart.opencart_docker.tests.pages.base_page import BaseComponent


class RegistrationPage(BaseComponent):
    DEFAULT_REGISTRATION_URL = 'http://localhost/index.php?route=account/register&language=en-gb'
    def __init__(
            self,
            context: 'BrowserContext',
            page: 'Page',
            rel_url: str = '',
            full_url: str = DEFAULT_REGISTRATION_URL,
            url_parameters: Optional[str] = None,
            request: Optional['pytest.FixtureRequest'] = None
    ):
        super().__init__(context, page, request)
        self.rel_url = rel_url
        self._full_url = full_url or ""
        self._url_parameters = url_parameters

        self.email_input = "#input-email"
        self.password_input = "#input-password"
        self.name_input = "#input-firstname"
        self.last_name = "#input-lastname"
        self.privacy_checkbox = 'input.form-check-input[name="agree"][type="checkbox"]'
        self.submit_button = "button[type='submit']"
        self.continue_button = "a.btn-primary:has-text('Continue')"

    def navigate_to_reg(self) -> None:
        """Navigate to registration page."""
        self.page.goto(self._full_url or self.rel_url)

    def fill_form(self, name: str, last_name: str, email: str, password: str) -> None:
        """Fill registration form."""
        self.page.fill(self.name_input, name)
        self.page.fill(self.last_name, last_name)
        self.page.fill(self.email_input, email)
        self.page.fill(self.password_input, password)

    def accept_privacy_policy(self) -> None:
        """Accept privacy policy in checkbox"""
        self.page.click(self.privacy_checkbox)

    def submit_form(self) -> None:
        """Submit registration form."""
        self.page.click("button[type='submit']")