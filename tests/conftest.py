import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from utils.screenshot_helper import save_screenshot
from utils.bug_report_generator import generate_bug_report


@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-save-password-bubble")
    chrome_options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        }
    )

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    driver.get("https://www.saucedemo.com/")

    yield driver

    driver.quit()


@pytest.fixture
def logged_in_driver(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    return driver


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver") or item.funcargs.get("logged_in_driver")

        if driver:
            screenshot_path = save_screenshot(
                driver,
                test_name=item.name
            )

            generate_bug_report(
                test_name=item.name,
                error_message=str(call.excinfo.value),
                screenshot_path=screenshot_path
            )
