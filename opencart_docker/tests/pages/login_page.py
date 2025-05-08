from typing import Optional

import pytest
from playwright.sync_api import BrowserContext, Page

from opencart_docker.tests.pages.base_page import BaseComponent


class LoginPage(BaseComponent):
    DEFAULT_LOGIN_PAGE = 'http://localhost/index.php?route=account/login&language=en-gb'
    def __init__(
            self,
            context: 'BrowserContext',
            page: 'Page',
            rel_url: str = '',
            full_url: str = DEFAULT_LOGIN_PAGE,
            url_parameters: Optional[str] = None,
            request: Optional['pytest.FixtureRequest'] = None
    ):
        super().__init__(context, page, request)
        self.rel_url = rel_url
        self._full_url = full_url or ""
        self._url_parameters = url_parameters

        self.continue_button = "a.btn-primary:has-text('Continue')"
        self.email_input = "#input-email"
        self.password_input = "#input-password"
        self.login_button = page.locator("button.btn.btn-primary", has_text="Login")

    def navigate_to_login(self) -> None:
         self.page.goto(self._full_url or self.rel_url)

    def fill_form(self, email: str, password: str) -> None:
        self.page.fill(self.email_input, email)
        self.page.fill(self.password_input, password)




