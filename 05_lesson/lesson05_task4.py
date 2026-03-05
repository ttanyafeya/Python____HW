# Открыть браузер FireFox.
# Перейти на страницу http://the-internet.herokuapp.com/login.
# В поле username ввести значение tomsmith.
# В поле password ввести значение SuperSecretPassword!.
# Нажать кнопку Login.
# Вывести текст с зеленой плашки в консоль.
# Закрыть браузер (метод quit()).

from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/login")

search_field = "input#username"
search_field = driver.find_element(By.CSS_SELECTOR, "input#username")
search_field.send_keys("tomsmith")

search_field = "input#password"
search_field = driver.find_element(By.CSS_SELECTOR, "input#password")
search_field.send_keys("SuperSecretPassword!")

button = driver.find_element(By.CSS_SELECTOR, "#login > button > i")
button.click()

flash = driver.find_element(By.CSS_SELECTOR, "div#flash")
print(flash.text)

sleep(5)
driver.quit()






sleep(5)