import allure
import pytest
import uuid
from playwright.sync_api import Page
from opencart_docker.tests.pages.registration_page import RegistrationPage


@allure.feature('User registration')
@allure.story('Register new user with valid credentials')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.registration
def test_user_registration(page: Page, clean_test_users):
    """Test successful user registration with valid credentials."""
    unique_id = uuid.uuid4().hex[:8]
    test_email = f'testuser_{unique_id}@example.com'
    test_password = 'SecurePass123!'

    registration_page = RegistrationPage(
        context=page.context,
        page=page,
        full_url="http://localhost/index.php?route=account/register"
    )

    with allure.step('1. Ensure logged out state'):
        page.goto('http://localhost/index.php?route=account/logout')
        page.click(registration_page.continue_button)

    with allure.step('2. Navigate to registration page'):
        registration_page.navigate()

    with allure.step('3. Fill registration form with valid details'):
        registration_page.fill_form(
            name=f'Test User {unique_id}',
            last_name=f'Test Lastname {unique_id}',
            email=test_email,
            password=test_password,
        )

    with allure.step('4. Accept privacy policy and submit the form'):
        registration_page.accept_privacy_policy()
        registration_page.submit_form()

    with allure.step('5. Verify successful registration'):
        assert "route=product/search" in page.url
        allure.attach(
            page.screenshot(full_page=True),
            name="post-registration",
            attachment_type=allure.attachment_type.PNG
        )