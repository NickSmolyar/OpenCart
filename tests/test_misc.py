import allure
import pytest

from playwright.sync_api import Page

from tests.conftest import contact_form_user
from tests.pages.unique_item_page import UniqueItemPage
from tests.pages.contact_form_page import ContactFormPage
from tests.pages.main_page import MainPage


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



















