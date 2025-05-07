import allure
import pytest
from faker import Faker
from playwright.sync_api import Page
from opencart_docker.tests.pages.registration_page import RegistrationPage


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
        full_url="http://localhost/index.php?route=account/register"
    )

    with allure.step('1. Ensure logged out state'):
        page.goto('http://localhost/index.php?route=account/logout')
        page.click(registration_page.continue_button)

    with allure.step('2. Register new user'):
        registration_page.navigate()
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


# @allure.feature('User registration')
# @allure.story('Register new user with valid credentials')
# @allure.severity(allure.severity_level.NORMAL)
# @pytest.mark.registration
# def test_user_registration_via_login_page(page: Page, clean_test_users):
#     """Test successful user registration with valid credentials on login page"""
#     unique_id = uuid.uuid4().hex[:8]
#     test_email = f'testuser_{unique_id}@example.com'
#     test_password = 'SecurePass123!'
#
# #
# #


