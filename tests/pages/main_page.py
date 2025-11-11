from typing import Optional

import pytest
from playwright.sync_api import BrowserContext, Page, Locator

from config.urls import URLs
from tests.pages.base_component import BaseComponent

class MainPage(BaseComponent):
    def __init__(
            self,
            context: BrowserContext,
            page: Page,
            request: Optional[pytest.FixtureRequest] = None
    ):
        super().__init__(context, page, request)
        self.url = URLs.BASE_URL

        self.currency_dropdown = page.locator("#form-currency")
        self.currency_dropdown_menu = page.locator("#form-currency .dropdown-menu.show")
        self.item_cart = page.locator(".btn.dropdown-toggle")
        self.product_carousel = page.locator("#carousel-banner-0.carousel")
        self.product_carousel_next_button = page.locator("button[data-bs-target='#carousel-banner-0'][data-bs-slide='next']")
        self.product_carousel_phone = page.locator('[alt*="iPhone 6"]')
        self.product_carousel_laptop = page.locator('[alt="MacBookAir"]')
        self.product_item = page.locator("#content .col")
        self.product_description = page.locator("[class*='content'] [class*='description']")
        self.add_to_cart_button = page.locator("button[type='submit'][title='Add to Cart']")
        self.success_alert = page.locator("[class*='alert-success']")
        self.item_cart_dropdown_menu = page.locator("[class*='dropdown-menu'] [class*='table-striped']")
        self.item_cart_remove_button = page.locator("[class*='btn-danger']")
        self.wishlist_button = page.locator("#wishlist-total")

    def open_main_page(self) -> None:
        self.page.goto(self.url)

    def currency_option(self, code: str) -> Locator:
        return self.page.locator(f".dropdown-menu .dropdown-item[href='{code}']")

    def click_add_to_cart_by_index(self, index: int = 0) -> None:
        button = self.add_to_cart_button.nth(index)
        button.wait_for()
        button.scroll_into_view_if_needed()
        button.click(force=True)

    def add_product_to_wishlist(self, product_name: str) -> None:
        wishlist_button = self.page.locator(
            f'.product-thumb:has-text("{product_name}") '
            '[formaction*="route=account/wishlist.add"]'
        ).first
        wishlist_button.wait_for(state="visible", timeout=5000)
        wishlist_button.scroll_into_view_if_needed()
        wishlist_button.click()







