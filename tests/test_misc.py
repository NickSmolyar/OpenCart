import re

import allure
import pytest
from playwright.sync_api import Page, expect

from tests.pages.contact_form_page import ContactFormPage
from tests.pages.login_page import LoginPage
from tests.pages.main_page import MainPage
from tests.pages.product_category_page import ProductCategoryPage
from tests.pages.unique_item_page import UniqueItemPage


@allure.feature('User contact form')
@allure.story('Contact form')
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.miscellaneous
def test_user_contact_form(context, page, contact_form_user):
    contact_form_page = ContactFormPage(context, page)
    success_message = page.locator("text=Your enquiry has been successfully sent to the store owner!")

    with allure.step('1. Fill form data'):
        contact_form_page.open_contact_form()
        contact_form_page.fill_contact_form(**contact_form_user)
        contact_form_page.submit_button.click()

    with allure.step('2. Verify successful enquiry'):
        expect(page).to_have_url(re.compile(r"route=information/contact"))
        assert success_message.is_visible


def test_carousel_item_opening(context, page):
    main_page = MainPage(context, page)
    item_page = UniqueItemPage(context, page)

    with allure.step('1. Open main page'):
        main_page.open_main_page()

    with allure.step('2. Click on phone item in carousel'):
        main_page.product_carousel_phone.click()
        item_page.product_description.wait_for()
        expect(page).to_have_url(re.compile(r"route=product/product"))
        assert "Samsung Galaxy" in item_page.product_description.text_content()

    with allure.step('3. Return to main page and check laptop'):
        main_page.open_main_page()
        main_page.product_carousel_next_button.click()
        main_page.product_carousel_laptop.click()
        expect(page).to_have_url(re.compile(r"route=common/home"))


@allure.feature('Product compare')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.miscellaneous
@pytest.mark.parametrize("product_name", [
    "Apple Cinema 30",
    "Canon EOS 5D",
])
def test_product_compare(context, page, static_user, product_name):
    login_page = LoginPage(context, page)
    category_page = ProductCategoryPage(context, page)

    with allure.step('1. Login to the application'):
        login_page.open_login_page()
        login_page.fill_form(**static_user)

        with page.expect_navigation():
            login_page.submit_login()

    with allure.step('2. Navigate to product category page'):
        category_page.open_product_category(category_id=20)
        page.wait_for_load_state('domcontentloaded')

    with allure.step(f'3. Add {product_name} to compare'):
        category_page.product_list.scroll_into_view_if_needed()
        category_page.add_product_to_compare(product_name)
        page.wait_for_timeout(1000)

    with allure.step('4. Navigate to compare page and verify'):
        category_page.product_compare_button.click()
        page.wait_for_load_state('networkidle')
        expect(page).to_have_url(re.compile(r"route=product/compare"))


@allure.feature('Product search')
@allure.story('Search functionality')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.miscellaneous
def test_product_search(context, page, static_user):
    login_page = LoginPage(context, page)

    with allure.step('1. Login to opencart'):
        login_page.open_login_page()
        login_page.fill_form(**static_user)
        login_page.submit_login()

    with allure.step('2. Search for product'):
        login_page.type_and_search('Iphone')

    with allure.step('3. Verify search results'):
        expect(page).to_have_url(re.compile(r"search=Iphone"))



















