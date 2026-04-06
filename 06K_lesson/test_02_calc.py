#Откройте страницу: https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html в Google Chrome.
# В поле ввода по локатору  #delay введите значение 45.
# Нажмите на кнопки:
# 7
# +
# 8
# =
# Проверьте (assert), что в окне отобразится результат 15 через 45 секунд.

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
#
# driver = webdriver.Chrome(
# service=ChromeService(ChromeDriverManager().install()))
#
# driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def test_slow_calculator():
    # Настройка браузера Chrome
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        # 1. Открыть страницу
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        # 2. В поле ввода по локатору #delay ввести значение 45
        delay_input = driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys("45")

        # 3. Нажать на кнопки: 7, +, 8, =
        # Используем поиск по тексту внутри кнопок (span)
        driver.find_element(By.XPATH, "//span[text()='7']").click()
        driver.find_element(By.XPATH, "//span[text()='+']").click()
        driver.find_element(By.XPATH, "//span[text()='8']").click()
        driver.find_element(By.XPATH, "//span[text()='=']").click()

        # 4. Проверить (assert), что в окне отобразится результат 15 через 45 секунд
        # Устанавливаем запас времени для ожидания (45 + 5 секунд)
        wait = WebDriverWait(driver, 50)

        # Ожидаем, пока текст в элементе с классом screen станет равным '15'
        wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))

        result_text = driver.find_element(By.CLASS_NAME, "screen").text
        assert result_text == "15", f"Ожидался результат 15, но получено: {result_text}"

    finally:
        # Закрыть браузер
        driver.quit()