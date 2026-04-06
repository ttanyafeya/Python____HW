import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.CalcPage import CalculatorPage


@pytest.fixture
def driver():
    # Настройка Chrome
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


def test_slow_calculator(driver):
    calc_page = CalculatorPage(driver)

    # 1. Открываем страницу
    calc_page.open()

    # 2. Вводим значение задержки 45
    calc_page.set_delay(45)

    # 3. Нажимаем кнопки 7, +, 8, =
    calc_page.click_button("7")
    calc_page.click_button("+")
    calc_page.click_button("8")
    calc_page.click_button("=")

    # 4. Проверяем, что результат 15 через 45 секунд
    # Мы передаем таймаут чуть больше 45, чтобы тест не упал по технической задержке
    result = calc_page.get_result(timeout=50)

    assert result == "15", f"Ожидался результат 15, но на экране: {result}"
