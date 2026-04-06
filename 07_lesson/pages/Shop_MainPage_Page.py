from selenium.webdriver.common.by import By

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_button = (By.CLASS_NAME, "shopping_cart_link")

    def add_to_cart(self, item_name):
        # Формируем ID кнопки на основе названия товара (нижний регистр и замена пробелов)
        item_id = item_name.lower().replace(" ", "-")
        locator = (By.ID, f"add-to-cart-{item_id}")
        self.driver.find_element(*locator).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_button).click()
