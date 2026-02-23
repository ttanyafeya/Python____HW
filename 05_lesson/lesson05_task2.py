# Клик по кнопке без ID
# Открыть браузер Google Chrome.
# Перейти на страницу: http://uitestingplayground.com/classattr.
# Кликнуть на синюю кнопку.

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

# открыть страницу
driver.get("http://uitestingplayground.com/dynamicid")

blue_button = driver.find_element(By.CLASS_NAME, "btn-primary")

blue_button.click()

sleep(10)

driver.quit()