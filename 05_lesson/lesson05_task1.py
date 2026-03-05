# Открыть браузер Google Chrome.
# Перейти на страницу: http://uitestingplayground.com/classattr.
# Кликнуть на синюю кнопку.

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.devtools.v142.fed_cm import click_dialog_button
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

# открыть страницу
driver.get("http://uitestingplayground.com/classattr")

blue_button = driver.find_element(By.CLASS_NAME, "btn-primary")

blue_button.click()

alert = driver.switch_to.alert
alert.accept()

sleep(10)

driver.quit()

