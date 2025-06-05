import allure
import pytest
import self

from playwright.sync_api import Page

from OpenCart.opencart_docker.tests.conftest import contact_form_user
from OpenCart.opencart_docker.tests.pages.contact_form_page import ContactFormPage

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
        assert success_message.is_visible()












