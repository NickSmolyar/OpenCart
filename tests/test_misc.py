import allure
import pytest
from playwright.sync_api import Page, expect
from tests.conftest import contact_form_user
from tests.pages.contact_form_page import ContactFormPage
from tests.pages.login_page import LoginPage
from tests.pages.main_page import MainPage
from tests.pages.product_category_page import ProductCategoryPage
from tests.pages.unique_item_page import UniqueItemPage


@allure.feature('User contact form')
@allure.story('Contact form')
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.miscellaneous
def test_user_contact_form(page: Page, contact_form_user):
    contact_form_page = ContactFormPage(
        context=page.context,
        page=page,
    )
    success_message = page.locator("text=Your enquiry has been successfully sent to the store owner!")
    with allure.step('1. Fill form data'):
        contact_form_page.open_contact_form()
        contact_form_page.fill_contact_form(**contact_form_user)
        contact_form_page.submit_button.click()

    with allure.step('2. Verify successful enquiry'):
        assert "route=information/contact" in page.url
        assert success_message.is_visible


def test_carousel_item_opening(page: Page):
    main_page = MainPage(page.context, page)
    item_page = UniqueItemPage(page.context, page)

    with allure.step('1. Open main page'):
        page.goto('http://localhost/index.php?route=common/home')

    with allure.step('2. Click on phone item in carousel'):
        main_page.product_carousel_phone.click()
        item_page.product_description.wait_for()
        assert "route=product/product" in page.url
        assert "Samsung Galaxy" in item_page.product_description.text_content()

    with allure.step('3. Return to main page'):
        page.goto('http://localhost/index.php?route=common/home')
        main_page.product_carousel_next_button.click()
        main_page.product_carousel_laptop.click()
        assert "route=common/home" in page.url


@pytest.mark.parametrize("product_name", [
    "Apple Cinema 30",
    "Canon EOS 5D",
])
def test_product_compare(page: Page, static_user, product_name):
    log_in_page = LoginPage(page.context, page)
    item_page = ProductCategoryPage(page.context, page)
    user_data_for_login = static_user

    with allure.step('1. Login to the application'):
        log_in_page.navigate_to_login()
        log_in_page.fill_form(**user_data_for_login)

        with page.expect_navigation():
            log_in_page.submit_login()

    with allure.step('2. Navigate to product category page'):
        page.goto('http://localhost/index.php?route=product/category&language=en-gb&path=20')
        page.wait_for_load_state('domcontentloaded')

    with allure.step(f'3. Add {product_name} to compare'):
        item_page.product_list.scroll_into_view_if_needed()
        item_page.compare_button.scroll_into_view_if_needed()

        product_element = item_page.get_product_by_name(product_name)
        item_page.add_product_to_compare(product_element=product_element)

        page.wait_for_timeout(1000)

    with allure.step('4. Navigate to compare page and verify'):
        item_page.product_compare_button.click()

        page.wait_for_load_state('networkidle')
        expect(page).to_have_url(lambda url: "route=product/compare" in url)
        expect(page.locator(f'text="{product_name}"')).to_be_visible()




















