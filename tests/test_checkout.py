from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage
import pytest
from utils.bug_report_generator import generate_bug_report


def test_checkout_information_form_success(logged_in_driver):
    driver = logged_in_driver

    inventory_page = InventoryPage(driver)
    assert inventory_page.is_loaded()

    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()

    cart_page = CartPage(driver)
    assert cart_page.is_loaded()
    assert cart_page.has_backpack()

    cart_page.click_checkout()

    assert "checkout-step-one" in driver.current_url

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_checkout_information("Test", "User", "12345")
    checkout_page.click_continue()

    assert "checkout-step-two" in driver.current_url

    checkout_overview_page = CheckoutOverviewPage(driver)

    assert checkout_overview_page.is_loaded()
    assert checkout_overview_page.has_backpack()

    checkout_overview_page.click_finish()

    assert "checkout-complete" in driver.current_url

@pytest.mark.parametrize(
    "first_name, last_name, postal_code, expected_error",
    [
        ("", "", "", "First Name is required"),
        ("", "User", "12345", "First Name is required"),
        ("Test", "", "12345", "Last Name is required"),
        ("Test", "User", "", "Postal Code is required"),
    ]
)
def test_checkout_validation_errors(
        logged_in_driver,
        first_name,
        last_name,
        postal_code,
        expected_error
):
    driver = logged_in_driver

    inventory_page = InventoryPage(driver)
    assert inventory_page.is_loaded()

    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()

    cart_page = CartPage(driver)
    assert cart_page.is_loaded()

    cart_page.click_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_checkout_information(
        first_name,
        last_name,
        postal_code
    )
    checkout_page.click_continue()

    assert expected_error in checkout_page.get_error_message()

def test_generate_bug_report():
    report_path = generate_bug_report(
        test_name="sample_failed_test",
        error_message="Element not found",
        screenshot_path="reports/screenshots/sample.png"
    )

    assert report_path is not None
