# Откройте сайт магазина: https://www.saucedemo.com/ в FireFox.
# Авторизуйтесь как пользователь standard_user.
# Добавьте в корзину товары:
# Sauce Labs Backpack.
# Sauce Labs Bolt T-Shirt.
# Sauce Labs Onesie.
# Перейдите в корзину.
# Нажмите Checkout.
# Заполните форму своими данными:
# имя,
# фамилия,
# почтовый индекс.
# Нажмите кнопку Continue.
# Прочитайте со страницы итоговую стоимость ( Total).
# Закройте браузер.
# Проверьте, что итоговая сумма равна  $58.29.
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.firefox import GeckoDriverManager
#
# driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
# driver.get("https://www.saucedemo.com/ ")

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager


def test_saucedemo_purchase():
    # Настройка браузера Firefox
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    try:
        # 1. Открыть сайт магазина
        driver.get("https://www.saucedemo.com/")

        # 2. Авторизоваться как standard_user
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # 3. Добавить товары в корзину
        # Sauce Labs Backpack
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        # Sauce Labs Bolt T-Shirt
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        # Sauce Labs Onesie
        driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

        # 4. Перейдите в корзину
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # 5. Нажмите Checkout
        driver.find_element(By.ID, "checkout").click()

        # 6. Заполните форму своими данными
        driver.find_element(By.ID, "first-name").send_keys("Иван")
        driver.find_element(By.ID, "last-name").send_keys("Иванов")
        driver.find_element(By.ID, "postal-code").send_keys("123456")

        # 7. Нажать кнопку Continue
        driver.find_element(By.ID, "continue").click()

        # 8. Прочитать итоговую стоимость (Total)
        # Ищем элемент с классом summary_total_label, который содержит текст "Total: $58.29"
        total_element = driver.find_element(By.CLASS_NAME, "summary_total_label")
        total_text = total_element.text  # Например: "Total: $58.29"

        # 9. Проверить, что итоговая сумма равна $58.29
        # Можно проверить вхождение подстроки или полное соответствие
        assert "58.29" in total_text, f"Ожидалась сумма $58.29, но на странице: {total_text}"
        assert total_text == "Total: $58.29"

    finally:
        # 10. Закрыть браузер
        driver.quit()