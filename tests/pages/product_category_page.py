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
        # self.compare_button = page.locator('[formaction="http://localhost/index.php?route=product/compare.add&language=en-gb"]')
        self.compare_added_popup = page.locator('[class ="alert alert-success alert-dismissible"]')
        self.product_compare_button = page.locator('[id="compare-total"]')
        self.product_list = page.locator('[id="product-list"]')

    def get_product_by_name(self, product_name: str):
        all_products = self.page.locator('.product-thumb .description h4 a')

        self.page.wait_for_function(
            "document.querySelectorAll('.product-thumb .description h4 a').length > 0"
        )

        count = all_products.count()
        for i in range(count):
            product = all_products.nth(i)
            product_text = product.text_content()

            if product_text and product_name.lower() in product_text.lower():
                return product

        raise ValueError(f"Product '{product_name}' not found on the page")

    def add_product_to_compare(self, product_name:str):
        compare_button = self.page.locator(
            f'.product-thumb:has-text("{product_name}") '
            '[formaction="http://localhost/index.php?route=product/compare.add&language=en-gb"]'
        ).first
        compare_button.wait_for(state="visible", timeout=5000)
        compare_button.scroll_into_view_if_needed()
        compare_button.click()

