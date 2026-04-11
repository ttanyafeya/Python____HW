import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import allure
from pages.CalcPage import CalculatorPage


@pytest.fixture
def driver():
    """Фикстура для настройки и завершения работы драйвера Chrome."""
    # Настройка Chrome
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


@allure.title("Проверка работы калькулятора с искусственной задержкой")
@allure.description("""
    Тест проверяет корректность работы калькулятора
     с установленной задержкой выполнения операций.

    Шаги теста:
    1. Открытие страницы калькулятора с искусственной задержкой
    2. Установка задержки 45 секунд
    3. Выполнение операции: 7 + 8
    4. Ожидание результата с учетом задержки
    5. Проверка, что результат равен 15

    Особенности:
    - Калькулятор имеет искусственную задержку перед выполнением операции
    - Таймаут ожидания результата установлен 50 секунд (чуть больше задержки)

    Ожидаемый результат: При сложении 7 и 8 должно получиться 15
""")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_slow_calculator(driver):
    """Тест проверки работы калькулятора с искусственной задержкой"""
    with allure.step("Инициализация страницы калькулятора"):
        calc_page = CalculatorPage(driver)
        allure.attach("Страница калькулятора создана",
                      name="Статус",
                      attachment_type=allure.attachment_type.TEXT)

    with allure.step("Открытие страницы калькулятора"):
        calc_page.open()
        allure.attach("https://bonigarcia.dev/"
                      "selenium-webdriver-java/slow-calculator.html",
                      name="URL страницы",
                      attachment_type=allure.attachment_type.URI_LIST)

    with allure.step("Установка задержки выполнения операций"):
        delay_seconds = 45
        calc_page.set_delay(delay_seconds)
        allure.attach(f"Задержка установлена на {delay_seconds} секунд",
                      name="Параметры задержки",
                      attachment_type=allure.attachment_type.TEXT)

    with allure.step("Ввод математического выражения: 7 + 8"):
        with allure.step("Нажатие кнопки '7'"):
            calc_page.click_button("7")
        with allure.step("Нажатие кнопки '+'"):
            calc_page.click_button("+")
        with allure.step("Нажатие кнопки '8'"):
            calc_page.click_button("8")
        with allure.step("Нажатие кнопки '=' для получения результата"):
            calc_page.click_button("=")

        allure.attach("Введено выражение: 7 + 8",
                      name="Математическое выражение",
                      attachment_type=allure.attachment_type.TEXT)

    with allure.step("Ожидание результата с учетом установленной задержки"):
        timeout = 50
        allure.attach(f"Таймаут ожидания установлен на {timeout} секунд",
                      name="Параметры ожидания",
                      attachment_type=allure.attachment_type.TEXT)
        result = calc_page.get_result(timeout=timeout)
        allure.attach(f"Полученный результат: {result}",
                      name="Результат вычисления",
                      attachment_type=allure.attachment_type.TEXT)

    with ((allure.step("Проверка корректности результата вычисления"))):
        expected_result = "15"
        allure.attach(f"Ожидаемый результат: {expected_result}",
                      name="Ожидание",
                      attachment_type=allure.attachment_type.TEXT)
        assert result == expected_result, (f"Ожидался "
                                           f"результат {expected_result},"
                                           f" но на экране: {result}")
        allure.attach("✓ Результат вычисления "
                      "совпадает с ожидаемым (7 + 8 = 15)",
                      name="Результат проверки",
                      attachment_type=allure.attachment_type.TEXT)
