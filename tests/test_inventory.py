from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_add_backpack_to_cart():
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)

    assert inventory_page.is_loaded()

    inventory_page.add_backpack_to_cart()

    assert inventory_page.get_cart_items_count() == "1"

    driver.quit()