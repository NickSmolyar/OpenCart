from typing import Optional

import pytest
from playwright.async_api import BrowserContext, Page

from config.urls import UNIQUE_ITEM_URL
from tests.pages.base_page import BaseComponent


class UniqueItemPage(BaseComponent):
    """
    Represents unique item page (e.g. tablet items/phone items) in OpenCart.
    Contains locators and methods to interact with account settings.
    """
    def __init__(
            self,
            context: 'BrowserContext',
            page: 'Page',
            rel_url: str = '',
            full_url: str = UNIQUE_ITEM_URL,
            url_parameters: Optional[str] = None,
            request: Optional['pytest.FixtureRequest'] = None
    ):
        super().__init__(context, page, request)
        self.rel_url = rel_url
        self._full_url = full_url or ""
        self._url_parameters = url_parameters

        self.product_description = page.locator('[id="product-info"] [class="col-sm"]:nth-child(2)')
