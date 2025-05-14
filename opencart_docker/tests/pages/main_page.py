from typing import Optional

import pytest
from playwright.sync_api import BrowserContext, Page

from OpenCart.opencart_docker.tests.pages.base_page import BaseComponent

class MainPage(BaseComponent):
    def __init__(
            self,
            context: 'BrowserContext',
            page: 'Page',
            rel_url: str = '',
            full_url: str = '',
            url_parameters: Optional[str] = None,
            request: Optional['pytest.FixtureRequest'] = None
    ):
        super().__init__(context, page, request)
        self.rel_url = rel_url
        self._full_url = full_url or ""
        self._url_parameters = url_parameters

        self.currency_dropdown = page.locator("#form-currency")
        self.currency_dropdown_menu = page.locator("#form-currency .dropdown-menu.show")
        self.item_cart = page.locator(".btn.dropdown-toggle")
        self.product_carousel = page.locator("#carousel-banner-0.carousel")
        self.product_item = page.locator("#content .col")

    def currency_option(self, code: str):
        return self.page.locator(f".dropdown-menu .dropdown-item[href='{code}']")






