import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from pages.Shop_Login_Page import LoginPage
from pages.Shop_MainPage_Page import MainPage
from pages.Shop_Card_Page import CartPage
from pages.Shop_Checkout_Page import CheckoutPage


@pytest.fixture
def driver():
    # Настройка Firefox
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    yield driver
    driver.quit()

def test_purchase_total(driver):
    login_page = LoginPage(driver)
    main_page = MainPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    # 1. Открыть сайт и авторизоваться
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # 2. Добавить товары в корзину
    main_page.add_to_cart("Sauce Labs Backpack")
    main_page.add_to_cart("Sauce Labs Bolt T-Shirt")
    main_page.add_to_cart("Sauce Labs Onesie")

    # 3. Перейти в корзину и нажать Checkout
    main_page.go_to_cart()
    cart_page.checkout()

    # 4. Заполнить форму данными
    checkout_page.fill_form("Ivan", "Ivanov", "123456")

    # 5. Прочитать итоговую стоимость
    total_val = checkout_page.get_total()

    # 6. Проверка итоговой суммы
    assert total_val == "58.29", f"Ожидалось 58.29, но получено {total_val}"