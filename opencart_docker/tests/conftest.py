import pymysql

import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()


@pytest.fixture
def clean_test_users():
    """Fixture to clean up test users from database after test."""
    yield
    connection = pymysql.connect(
        host="localhost",
        port=3306,
        user="user",
        password="password",
        database="opencart"
    )
    try:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM oc_customer WHERE email LIKE 'testuser_%@example.com'")
            connection.commit()
    finally:
        connection.close()


@pytest.fixture
def static_user():
    return {
        'email': 'testuser@email.com',
        'password': 'randompass',
    }

