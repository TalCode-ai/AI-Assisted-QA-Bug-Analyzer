from selenium.webdriver.common.by import By


class CartPage:
    CART_TITLE = (By.CLASS_NAME, "title")
    BACKPACK_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")

    def __init__(self, driver):
        self.driver = driver

    def is_loaded(self):
        return self.driver.find_element(*self.CART_TITLE).text == "Your Cart"

    def get_product_name(self):
        return self.driver.find_element(*self.BACKPACK_ITEM_NAME).text

    def has_backpack(self):
        return self.get_product_name() == "Sauce Labs Backpack"

    def click_checkout(self):
        checkout_button = self.driver.find_element(*self.CHECKOUT_BUTTON)
        self.driver.execute_script("arguments[0].click();", checkout_button)

    def click_continue_shopping(self):
        self.driver.find_element(*self.CONTINUE_SHOPPING_BUTTON).click()