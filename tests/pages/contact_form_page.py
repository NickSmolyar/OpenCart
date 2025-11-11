from typing import Optional
import pytest
from playwright.sync_api import BrowserContext, Page

from config.urls import URLs
from tests.pages.base_component import BaseComponent


class ContactFormPage(BaseComponent):
    def __init__(
            self,
            context: BrowserContext,
            page: Page,
            request: Optional[pytest.FixtureRequest] = None
    ):
        super().__init__(context, page, request)
        self.url = URLs.CONTACT_FORM

        self.name_input = page.locator("#input-name")
        self.email_input = page.locator("#input-email")
        self.enquiry_textarea = page.locator("#input-enquiry")
        self.submit_button = page.locator("button.btn-primary[type='submit']")

    def open_contact_form(self) -> None:
        self.page.goto(self.url)

    def fill_contact_form(self, name: str, email: str, enquiry: str) -> None:
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.enquiry_textarea.fill(enquiry)

    def click_submit(self) -> None:
        self.submit_button.click()

    def fill_name(self, name: str) -> None:
        self.name_input.fill(name)

    def fill_email(self, email: str) -> None:
        self.email_input.fill(email)

    def fill_enquiry(self, enquiry: str) -> None:
        self.enquiry_textarea.fill(enquiry)

    def get_name_value(self) -> str:
        return self.name_input.input_value()

    def get_email_value(self) -> str:
        return self.email_input.input_value()

    def get_enquiry_value(self) -> str:
        return self.enquiry_textarea.input_value()