from typing import Optional

import pytest
from playwright.async_api import BrowserContext, Page

from config.urls import PRODUCT_CATEGORY_URL
from tests.pages.base_page import BaseComponent


def get_product_by_name(page, product_name=None):
    if product_name:
        return page.locator('[id="product-list"] [class="product-thumb"] [class="description"]').filter(has_text=product_name)
    else:
        return page.locator('[id="product-list"] [class="product-thumb"] [class="description"]').first()


def add_product_to_compare(page: Page, **kwargs):
    product_name = kwargs.get('product_name')
    product_element = kwargs.get('product_element')

    if product_element:
        product = product_element
    elif product_name:
        product = get_product_by_name(page, product_name)
    else:
        raise ValueError("Either product_name or product_element must be provided")


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
        self.rel_url = rel_url
        self._full_url = full_url or ""
        self._url_parameters = url_parameters

        self.product_item = page.locator('[id="product-list"] [class="product-thumb"]')
        self.compare_button = page.locator('[data-bs-original-title="Compare this Product"]')
        self.compare_added_popup = page.locator('[class ="alert alert-success alert-dismissible"]')
        self.product_compare_button = page.locator('[id="compare-total"]')
