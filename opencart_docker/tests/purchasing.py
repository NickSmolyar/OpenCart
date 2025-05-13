import allure
import pytest
from faker import Faker
from playwright.sync_api import Page

from OpenCart.opencart_docker.tests.pages import registration_page
from OpenCart.opencart_docker.tests.pages.main_page import MainPage

@allure.feature('Currency conversion')
@allure.story('Check currency conversion')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.purchasing
def test_currency_conversion(page: Page):

    main_page = MainPage(page)

    with allure.step('1. Open main page'):
        page.goto('http://localhost/index.php?route=common/home')
        page.click(main_page.currency_dropdown)

    with allure.step('2. Choose different currency'):


