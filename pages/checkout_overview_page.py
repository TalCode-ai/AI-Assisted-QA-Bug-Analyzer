from selenium.webdriver.common.by import By


class CheckoutOverviewPage:
    OVERVIEW_TITLE = (By.CLASS_NAME, "title")
    FINISH_BUTTON = (By.ID, "finish")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self, driver):
        self.driver = driver

    def is_loaded(self):
        return self.driver.find_element(*self.OVERVIEW_TITLE).text == "Checkout: Overview"

    def has_backpack(self):
        return self.driver.find_element(*self.ITEM_NAME).text == "Sauce Labs Backpack"

    def click_finish(self):
        self.driver.find_element(*self.FINISH_BUTTON).click()