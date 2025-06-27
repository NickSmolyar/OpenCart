import allure
import pytest

from playwright.sync_api import Page
from OpenCart.opencart_docker.tests.pages.main_page import MainPage

@allure.feature('Currency conversion')
@allure.story('Check currency conversion')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.purchasing
@pytest.mark.parametrize("currency_code,symbol", [
    ("EUR", "€"),
    ("GBP", "£"),
    ("USD", "$")
])
def test_currency_conversion(page: Page, currency_code, symbol):
    """Test successful currency conversion on main page."""
    main_page = MainPage(
        context=page.context,
        page=page,
    )

    with allure.step('1. Open main page'):
        page.goto('http://localhost/index.php?route=common/home')
        main_page.currency_dropdown.click()

    with allure.step(f'2. Choose {currency_code} currency'):
        main_page.currency_option(currency_code).click()
        page.wait_for_selector('#form-currency', state='attached')

    with allure.step('3. Currency changed successfully'):
        dropdown_text = main_page.currency_dropdown.text_content()
        assert symbol in dropdown_text, f"Expected symbol {symbol} in dropdown text: {dropdown_text}"
        screenshot_path = main_page.make_screenshot("currency_conversion")
        allure.attach.file(
            screenshot_path,
            name="Currency Conversion Screenshot",
            attachment_type=allure.attachment_type.PNG
        )


@allure.feature('Adding item to cart')
@allure.story('Check functionality of item cart')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.purchasing
def test_add_to_cart_functionality(page: Page):
    main_page = MainPage(
        context=page.context,
        page=page,
    )

    with allure.step('1. Open main page'):
        page.goto('http://localhost/index.php?route=common/home')

    with allure.step('2. Add item to cart and open it'):
        main_page.click_add_to_cart_by_index(1)
        main_page.success_alert.wait_for()
        assert main_page.success_alert.is_visible

    with allure.step('3. Check item cart status on main page'):
        main_page.item_cart.click()
        main_page.item_cart_dropdown_menu.wait_for()
        text = main_page.item_cart_dropdown_menu.inner_text()
        assert 'iPhone' in text

    with allure.step('4. Remove item from cart and verify alert'):
        main_page.item_cart_remove_button.click()
        main_page.success_alert.wait_for()
        assert main_page.success_alert.is_visible









