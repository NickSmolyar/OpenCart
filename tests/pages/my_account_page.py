from typing import Optional

import pytest
from playwright.sync_api import BrowserContext, Page

from config.urls import URLs
from tests.pages.base_component import BaseComponent


class MyAccountPage(BaseComponent):
    """
    Represents the 'My Account' page in OpenCart.
    Contains locators and methods to interact with account settings.
    """
    def __init__(
            self,
            context: BrowserContext,
            page: Page,
            request: Optional[pytest.FixtureRequest] = None
    ):
        super().__init__(context, page, request)
        self.url = URLs.MY_ACCOUNT

        #My account section
        self.edit_account_info = page.locator('.list-unstyled a[href*="route=account/edit"]')
        self.change_password = page.locator('.list-unstyled a[href*="route=account/password"]')
        self.stored_payment_methods = page.locator('.list-unstyled a[href*="route=account/payment_method"]')
        self.modify_address_book = page.locator('.list-unstyled a[href*="route=account/address"]')
        self.modify_wishlist = page.locator('.list-unstyled a[href*="route=account/wishlist"]')

        # My orders section
        self.view_order_history = page.locator('.list-unstyled a[href*="route=account/order"]')
        self.order_subscriptions = page.locator('.list-unstyled a[href*="route=account/subscription"]')
        self.order_downloads = page.locator('.list-unstyled a[href*="route=account/download"]')
        self.reward_points = page.locator('.list-unstyled a[href*="route=account/reward"]')
        self.order_return_requests = page.locator('.list-unstyled a[href*="route=account/returns"]')
        self.order_transactions = page.locator('.list-unstyled a[href*="route=account/transaction"]')

        #Misc
        self.affiliate_account = page.locator('.list-unstyled a[href*="route=account/affiliate"]')
        self.account_newsletter = page.locator('.list-unstyled a[href*="route=account/newsletter"]')

        #Generic fields
        self.account_name_input = page.locator("#input-firstname")
        self.account_last_name = page.locator("#input-lastname")
        self.account_email_input = page.locator("#input-email")
        self.continue_button = page.locator(".btn-primary")
        self.success_alert = page.locator(".alert alert-success alert-dismissible")

    def open_my_account_page(self) -> None:
        self.page.goto(self.url)

    def fill_form(self, name: str, last_name: str, email: str) -> None:
        self.account_name_input.fill(name)
        self.account_last_name.fill(last_name)
        self.account_email_input.fill(email)

    def submit_form(self) -> None:
        self.continue_button.click()