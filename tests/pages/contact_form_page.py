from typing import Optional

import pytest
from playwright.async_api import BrowserContext, Page

from config.urls import CONTACT_FORM_URL
from tests.pages.base_page import BaseComponent

class ContactFormPage(BaseComponent):
    def __init__(
            self,
            context: 'BrowserContext',
            page: 'Page',
            rel_url: str = '',
            full_url: str = CONTACT_FORM_URL,
            url_parameters: Optional[str] = None,
            request: Optional['pytest.FixtureRequest'] = None
    ):
        super().__init__(context, page, request)
        self.rel_url = rel_url
        self._full_url = full_url or ""
        self._url_parameters = url_parameters

        self.name_input = "#input-name"
        self.email_address = "#input-email"
        self.enquiry_form = "#input-enquiry"

        self.submit_button = page.locator("button.btn-primary[type='submit']")

    def open_contact_form(self) -> None:
         self.page.goto(self._full_url or self.rel_url)

    def fill_contact_form(self, name: str, email: str, enquiry: str) -> None:
        self.page.fill(self.name_input, name)
        self.page.fill(self.email_address, email)
        self.page.fill(self.enquiry_form, enquiry)