import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import allure
from pages.Shop_Login_Page import LoginPage
from pages.Shop_MainPage_Page import MainPage
from pages.Shop_Card_Page import CartPage
from pages.Shop_Checkout_Page import CheckoutPage


@pytest.fixture
def driver():

    """
    Фикстура для настройки
    и завершения работы драйвера Firefox.

    """

    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    yield driver
    driver.quit()


@allure.title("Проверка итоговой суммы покупки"
              " в интернет-магазине SauceDemo")
@allure.description("""
    Тест проверяет корректность расчета итоговой стоимости
    при добавлении трех товаров в корзину.

    Шаги теста:
    1. Авторизация на сайте под стандартным пользователем
    2. Добавление трех товаров в корзину: Sauce Labs Backpack,
       Sauce Labs Bolt T-Shirt, Sauce Labs Onesie
    3. Переход в корзину и начало оформления заказа
    4. Заполнение формы доставки (имя, фамилия, почтовый индекс)
    5. Получение итоговой суммы заказа
    
    6. Сравнение полученной суммы с ожидаемым значением 58.29
    Ожидаемый результат: Итоговая сумма должна быть равна $58.29
    """)
@allure.feature("Оформление заказа")
@allure.severity(allure.severity_level.CRITICAL)
def test_purchase_total(driver):

    """Тест проверки итоговой суммы покупки."""

    with allure.step("Инициализация"
                     " страниц приложения"):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

    with allure.step("Открытие страницы авторизации и вход в систему"):
        login_page.open()
        login_page.login("standard_user",
                         "secret_sauce")
        allure.attach("standard_user",
                      name="Имя пользователя",
                      attachment_type=allure.attachment_type.TEXT)

    with allure.step("Добавление товаров в корзину"):
        items = ["Sauce Labs Backpack",
                 "Sauce Labs Bolt T-Shirt",
                 "Sauce Labs Onesie"]
        for item in items:
            with allure.step(f"Добавление товара: {item}"):
                main_page.add_to_cart(item)
        allure.attach(", ".join(items),
                      name="Добавленные товары",
                      attachment_type=allure.attachment_type.TEXT)

    with allure.step("Переход в корзину и начало оформления заказа"):
        main_page.go_to_cart()
        cart_page.checkout()
        allure.attach("Клик по кнопке Checkout",
                      name="Действие",
                      attachment_type=allure.attachment_type.TEXT)

    with allure.step("Заполнение формы доставки"):
        checkout_page.fill_form("Ivan",
                                "Ivanov",
                                "123456")
        allure.attach(
            "Имя: Ivan,"
            " Фамилия: Ivanov,"
            " Почтовый индекс: 123456",
            name="Данные покупателя",
            attachment_type=allure.attachment_type.TEXT
        )

    with allure.step("Получение итоговой стоимости заказа"):
        total_val = checkout_page.get_total()
        allure.attach(f"Полученная сумма: ${total_val}",
                      name="Итоговая стоимость",
                      attachment_type=allure.attachment_type.TEXT)

    with (allure.step("Проверка итоговой суммы заказа")):
        expected_total = "58.29"
        allure.attach(f"Ожидаемая сумма: ${expected_total}", name="Ожидание",
                      attachment_type=allure.attachment_type.TEXT)
        assert total_val == expected_total, (f"Ожидалось {expected_total},"
                                             f" но получено {total_val}")
        allure.attach("✓ Итоговая сумма совпадает с ожидаемой",
                      name="Результат проверки",
                      attachment_type=allure.attachment_type.TEXT)
