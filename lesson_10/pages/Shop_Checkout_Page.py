from selenium.webdriver.common.by import By


class CheckoutPage:
    """
    Page Object Model для страницы оформления заказа интернет-магазина.

    Предоставляет методы для заполнения платежной информации и получения
    итоговой стоимости заказа на этапе оформления покупки.
    """

    def __init__(self, driver) -> None:
        """
        Инициализация страницы оформления заказа.

        Сохраняет экземпляр WebDriver и инициализирует локаторы для всех
        элементов формы оформления заказа: поля ввода персональных данных,
        кнопка продолжения и отображение итоговой суммы.

        """
        self.driver = driver
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.zip_code = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    def fill_form(self, first: str, last: str, zip_idx: str) -> None:
        """
        Заполняет форму оформления заказа и переходит к следующему шагу.

        Вводит имя, фамилию и почтовый индекс в соответствующие поля формы,
        затем автоматически нажимает кнопку "Continue"
        для перехода к следующему этапу оформления заказа
        (обычно к странице подтверждения или оплаты).

        """
        self.driver.find_element(*self.first_name).send_keys(first)
        self.driver.find_element(*self.last_name).send_keys(last)
        self.driver.find_element(*self.zip_code).send_keys(zip_idx)
        self.driver.find_element(*self.continue_button).click()

    def get_total(self) -> str:
        """
        Извлекает итоговую сумму заказа из текстовой метки.

        Находит элемент с итоговой суммой, извлекает его текст,
        парсит строку и возвращает только числовое значение суммы
        (удаляя текстовый префикс, например "Total: $").

        """
        total_text = self.driver.find_element(*self.total_label).text
        return total_text.split("$")[-1]
