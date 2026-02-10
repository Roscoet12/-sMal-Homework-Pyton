from selenium.webdriver.common.by import By
import allure

class Main:
    """
    Этот класс представляет страницу авторизации в магазине
    """
    def __init__(self, browser):
        self.driver = browser
        self.driver.implicitly_wait(10)

    @allure.step('Открыть страницу магазина в браузере Firefox')
    def get_browser(self) -> None:
        """
        Эта функция открывает страницу магазина в браузере Firefox"""
        self.driver.get('https://www.saucedemo.com/')

    @allure.step('Заполнить поля для авторизации валидными данными. '
                 'Кликнуть на кнопку Авторизоваться')
    def autorization(self, user_name: str, password: str) -> None:
        """
        Эта функция заполняет форму для авторизации и кликает на кнопку Авторизоваться.
        Принимаемые на ввод данные - Имя пользователя, Пароль.
        """
        self.driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys(user_name)
        self.driver.find_element(By.CSS_SELECTOR, '#password').send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, '#login-button').click()
