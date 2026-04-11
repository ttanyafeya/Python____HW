from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """
    Page Object Model для страницы калькулятора с задержкой.
    Предоставляет методы для взаимодействия с веб-элементами калькулятора,
    который имеет искусственную задержку перед выполнением операций.
    """

    def __init__(self, driver) -> None:
        """
        Инициализация страницы калькулятора.

        Устанавливает WebDriver, URL страницы
        и локаторы для основных элементов.

        """
        self.driver = driver
        self.url = ("https://bonigarcia.dev/"
                    "selenium-webdriver-java/slow-calculator.html")
        self.delay_input = (By.ID, "delay")
        self.screen = (By.CLASS_NAME, "screen")

    def open(self) -> None:
        """
        Открывает страницу калькулятора в браузере.

        Использует текущий экземпляр WebDriver для перехода по URL,
        сохраненному в атрибуте self.url.

        """
        self.driver.get(self.url)

    def set_delay(self, seconds: int) -> None:
        """
        Устанавливает время искусственной задержки для калькулятора.

        Находит поле ввода задержки, очищает его текущее содержимое
        и вводит указанное количество секунд. Калькулятор будет ждать
        это время перед выполнением каждой операции.

        """
        delay_field = self.driver.find_element(*self.delay_input)
        delay_field.clear()
        delay_field.send_keys(str(seconds))

    def click_button(self, text: str) -> None:
        """
        Нажимает на кнопку калькулятора с указанным текстом.

        Ищет кнопку по точному совпадению текста внутри тега <span>.
        Поддерживает как цифры (0-9), так и операторы (+, -, ×, /, =).

        """
        xpath = f"//span[text()='{text}']"
        self.driver.find_element(By.XPATH, xpath).click()

    def get_result(self, timeout: int = 50) -> str:
        """
        Получает результат вычисления с ожиданием появления значения "15".

        Ожидает, пока на экране калькулятора не появится текст "15".
        После появления результата возвращает текст с экрана.

        """
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.text_to_be_present_in_element(self.screen, "15"))
        return self.driver.find_element(*self.screen).text
