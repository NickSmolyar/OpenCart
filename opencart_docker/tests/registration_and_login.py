import allure
import pytest
from faker import Faker
from playwright.sync_api import Page

from conftest import static_user
from OpenCart.opencart_docker.tests.pages.login_page import LoginPage
from OpenCart.opencart_docker.tests.pages.registration_page import RegistrationPage


@allure.feature('User registration')
@allure.story('Register new user with valid credentials')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.registration
def test_user_registration_via_main(page: Page, clean_test_users):
    """Test successful user registration with valid credentials."""
    fake = Faker()
    user_data = {
        'name': fake.first_name(),
        'last_name': fake.last_name(),
        'email': fake.email(),
        'password': fake.password(length=8, special_chars=True),
    }

    registration_page = RegistrationPage(
        context=page.context,
        page=page,
    )

    with allure.step('1. Ensure logged out state'):
        page.goto('http://localhost/index.php?route=account/logout')
        page.click(registration_page.continue_button)

    with allure.step('2. Register new user'):
        registration_page.navigate_to_reg()
        registration_page.fill_form(**user_data)

    with allure.step('3. Accept privacy policy and submit the form'):
        registration_page.accept_privacy_policy()
        registration_page.submit_form()

    with allure.step('4. Verify successful registration'):
        assert "route=product/search" in page.url
        allure.attach(
            page.screenshot(full_page=True),
            name="post-registration",
            attachment_type=allure.attachment_type.PNG
        )


@allure.feature('User login')
@allure.story('Login user with valid credentials')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.registration
def test_user_registration_via_login_page(page: Page, static_user):
    """Test successful user login with valid credentials."""
    user_data = static_user
    login_page = LoginPage(
        context=page.context,
        page=page,
    )

    with allure.step('1. Ensure logged out state'):
        page.goto('http://localhost/index.php?route=account/logout')

    with allure.step('2. Login user'):
        login_page.navigate_to_login()
        login_page.fill_form(**user_data)
        login_page.login_button.click()

    with allure.step('3. Verify successful login'):
        assert "route=account/login" in page.url
        allure.attach(
            page.screenshot(full_page=True),
            name="post-login",
            attachment_type=allure.attachment_type.PNG
        )











