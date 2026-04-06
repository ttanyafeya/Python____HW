from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        self.delay_input = (By.ID, "delay")
        self.screen = (By.CLASS_NAME, "screen")

    def open(self):
        self.driver.get(self.url)

    def set_delay(self, seconds):
        delay_field = self.driver.find_element(*self.delay_input)
        delay_field.clear()
        delay_field.send_keys(str(seconds))

    def click_button(self, text):
        # Поиск кнопки по тексту внутри тега span
        xpath = f"//span[text()='{text}']"
        self.driver.find_element(By.XPATH, xpath).click()

    def get_result(self, timeout=50):
        # Ожидание появления текста "15" в окне результата
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.text_to_be_present_in_element(self.screen, "15"))
        return self.driver.find_element(*self.screen).text