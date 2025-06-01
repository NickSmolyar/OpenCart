from typing import Optional

import pytest

from OpenCart.opencart_docker.config.urls import MY_ACCOUNT_URL
from playwright.sync_api import BrowserContext, Page
from OpenCart.opencart_docker.tests.pages.login_page import LoginPage


class MyAccountPage(LoginPage):
    """
    Represents the 'My Account' page in OpenCart.
    Contains locators and methods to interact with account settings.
    """
    def __init__(
            self,
            context: 'BrowserContext',
            page: 'Page',
            rel_url: str = '',
            full_url: str = MY_ACCOUNT_URL,
            url_parameters: Optional[str] = None,
            request: Optional['pytest.FixtureRequest'] = None
    ):
        super().__init__(context, page, request)
        self.rel_url = rel_url
        self._full_url = full_url or ""
        self._url_parameters = url_parameters

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

        self.affiliate_account = page.locator('.list-unstyled a[href*="route=account/affiliate"]')
        self.account_newsletter = page.locator('.list-unstyled a[href*="route=account/newsletter"]')

        #Generic fields
        self.name_input = page.locator("#input-firstname")
        self.last_name = page.locator("#input-lastname")
        self.email_input = page.locator("#input-email")
        self.continue_button = page.locator("a.btn-primary:has-text('Continue')")