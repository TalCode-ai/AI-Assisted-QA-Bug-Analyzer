from selenium.webdriver.common.by import By


class InventoryPage:
    PRODUCTS_TITLE = (By.CLASS_NAME, "title")
    ADD_BACKPACK_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    SHOPPING_CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver):
        self.driver = driver

    def is_loaded(self):
        return self.driver.find_element(*self.PRODUCTS_TITLE).text == "Products"

    def add_backpack_to_cart(self):
        self.driver.find_element(*self.ADD_BACKPACK_BUTTON).click()

    def open_cart(self):
        self.driver.find_element(*self.SHOPPING_CART_LINK).click()

    def get_cart_items_count(self):
        return self.driver.find_element(*self.SHOPPING_CART_BADGE).text