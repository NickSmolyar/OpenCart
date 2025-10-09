from typing import Optional

import pytest
from playwright.sync_api import BrowserContext, Page, expect

from config.urls import PRODUCT_CATEGORY_URL
from tests.pages.base_page import BaseComponent


class ProductCategoryPage(BaseComponent):
    def __init__(
            self,
            context: 'BrowserContext',
            page: 'Page',
            rel_url: str = '',
            full_url: str = PRODUCT_CATEGORY_URL,
            url_parameters: Optional[str] = None,
            request: Optional['pytest.FixtureRequest'] = None
    ):
        super().__init__(context, page, request)
        self.page = page   # store the Playwright page instance
        self.rel_url = rel_url
        self._full_url = full_url or ""
        self._url_parameters = url_parameters

        self.product_item = page.locator('[id="product-list"] [class="product-thumb"]')
        self.compare_added_popup = page.locator('[class ="alert alert-success alert-dismissible"]')
        self.product_compare_button = page.locator('[id="compare-total"]')
        self.product_list = page.locator('[id="product-list"]')

    def add_product_to_compare(self, product_name:str):
        compare_button = self.page.locator(
            f'.product-thumb:has-text("{product_name}") '
            '[formaction="http://localhost/index.php?route=product/compare.add&language=en-gb"]'
        ).first
        compare_button.wait_for(state="visible", timeout=5000)
        compare_button.scroll_into_view_if_needed()
        compare_button.click()

    def add_product_to_wishlist(self, product_name:str):
        wishlist_button = self.page.locator(
            f'.product-thumb:has-text("{product_name}") '
            '[formaction="http://localhost/index.php?route=account/wishlist.add&language=en-gb"]'
        ).first
        wishlist_button.wait_for(state="visible", timeout=5000)
        wishlist_button.scroll_into_view_if_needed()
        wishlist_button.click()

