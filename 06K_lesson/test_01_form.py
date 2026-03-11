import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    # Настройка драйвера для Edge
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_form_validation(driver):
    # 1. Открываем страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # 2. Заполняем форму
    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    # Поле Zip code оставляем пустым
    driver.find_element(By.NAME, "zip-code").clear()

    # 3. Нажимаем кнопку Submit
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Ожидание появления результатов валидации
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, "zip-code")))

    # 4. Проверяем, что поле Zip code подсвечено красным
    # В данной верстке класс 'alert-danger' отвечает за красную подсветку
    zip_code_class = driver.find_element(By.ID, "zip-code").get_attribute("class")
    assert "alert-danger" in zip_code_class

    # 5. Проверяем, что остальные поля подсвечены зеленым
    fields = [
        "first-name",
        "last-name",
        "address",
        "e-mail",
        "phone",
        "city",
        "country",
        "job-position",
        "company"
    ]

    for field_id in fields:
        field_class = driver.find_element(By.ID, field_id).get_attribute("class")
        assert "alert-success" in field_class, f"Поле {field_id} не подсвечено зеленым"