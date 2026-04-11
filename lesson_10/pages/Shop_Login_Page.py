from selenium.webdriver.common.by import By


class LoginPage:
    """
    Page Object Model для страницы авторизации SauceDemo.

    Предоставляет методы для открытия страницы логина и выполнения
    аутентификации пользователя на тестовом интернет-магазине SauceDemo.
    """

    def __init__(self, driver):
        """
        Инициализация страницы авторизации.

        Сохраняет экземпляр WebDriver, устанавливает URL страницы логина
        и инициализирует локаторы для всех элементов формы входа.

        """
        self.driver = driver
        self.url = "https://www.saucedemo.com/"
        self.username_field: tuple = (By.ID, "user-name")
        self.password_field: tuple = (By.ID, "password")
        self.login_button: tuple = (By.ID, "login-button")

    def open(self) -> None:
        """
        Открывает страницу авторизации в браузере.

        Использует текущий экземпляр WebDriver для перехода на URL
        страницы логина SauceDemo. После вызова метода страница
        загружается и становится доступной для взаимодействия.

        """
        self.driver.get(self.url)

    def login(self, username: str, password: str) -> None:
        """
        Выполняет вход в систему с указанными учетными данными.

        Заполняет поля имени пользователя и пароля переданными значениями,
        затем нажимает кнопку "Login" для отправки формы аутентификации.
        После успешного входа происходит перенаправление на главную страницу
        интернет-магазина.

        """
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()
