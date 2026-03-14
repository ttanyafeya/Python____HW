from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.zip_code = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    def fill_form(self, first, last, zip_idx):
        self.driver.find_element(*self.first_name).send_keys(first)
        self.driver.find_element(*self.last_name).send_keys(last)
        self.driver.find_element(*self.zip_code).send_keys(zip_idx)
        self.driver.find_element(*self.continue_button).click()

    def get_total(self):
        total_text = self.driver.find_element(*self.total_label).text
        # Извлекаем только числовое значение после "Total: $"
        return total_text.split("$")[-1]