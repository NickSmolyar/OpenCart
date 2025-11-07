from typing import Optional
import pytest
from playwright.sync_api import BrowserContext, Page

from config.urls import URLs
from tests.pages.base_component import BaseComponent


class ContactFormPage(BaseComponent):
    NAME_INPUT = "#input-name"
    EMAIL_INPUT = "#input-email"
    ENQUIRY_TEXTAREA = "#input-enquiry"
    SUBMIT_BUTTON = "button.btn-primary[type='submit']"

    def __init__(
            self,
            context: BrowserContext,
            page: Page,
            request: Optional[pytest.FixtureRequest] = None
    ):
        super().__init__(context, page, request)
        self.url = URLs.CONTACT_FORM

    def open_contact_form(self) -> None:
        self.page.goto(self.url)

    def fill_contact_form(self, name: str, email: str, enquiry: str) -> None:
        self.page.fill(self.NAME_INPUT, name)
        self.page.fill(self.EMAIL_INPUT, email)
        self.page.fill(self.ENQUIRY_TEXTAREA, enquiry)

    def click_submit(self) -> None:
        self.page.click(self.SUBMIT_BUTTON)

    def fill_name(self, name: str) -> None:
        self.page.fill(self.NAME_INPUT, name)

    def fill_email(self, email: str) -> None:
        self.page.fill(self.EMAIL_INPUT, email)

    def fill_enquiry(self, enquiry: str) -> None:
        self.page.fill(self.ENQUIRY_TEXTAREA, enquiry)

    def get_name_value(self) -> str:
        return self.page.input_value(self.NAME_INPUT)

    def get_email_value(self) -> str:
        return self.page.input_value(self.EMAIL_INPUT)

    def get_enquiry_value(self) -> str:
        return self.page.input_value(self.ENQUIRY_TEXTAREA)