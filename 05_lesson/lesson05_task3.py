# Открыть браузер FireFox.
# Перейти на страницу: http://the-internet.herokuapp.com/inputs.
# Ввести в поле текст Sky.
# Очистить это поле (метод clear()).
# Ввести в поле текст Pro.
# Закрыть браузер (метод quit()).


from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/inputs")


search_field = "input"
search_field = driver.find_element(By.CSS_SELECTOR, "input")

search_field.send_keys("Sky")
sleep(5)
search_field.clear()

search_field.send_keys("Pro")
sleep(5)
search_field.clear()

sleep(5)
driver.quit()