import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Main:
    """
    Этот класс представляет страницу калькулятора.
    У страницы есть поле для заполнения - сколько секунд калькулятор ждет.
    """
    def __init__(self, browser):
        self.driver = browser

    @allure.step('Открыть страницу калькулятор в браузере Chrome ')
    def get_browser(self) -> None:
        """
        Эта функция открывает страницу с калькулятором в Chrome
        """
        self.driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

    @allure.step('Ввести время ожидания')
    def change_expectation(self, expectation: int) -> None:
        """
        Эта функция чистит базовое время ожидания и вводит необходимое.
        Время ожидание должно быть в секундах.
        """
        self.driver.find_element(By.CSS_SELECTOR, '#delay').clear()
        self.driver.find_element(By.CSS_SELECTOR, '#delay').send_keys(expectation)

    @allure.step('Ввести пример на вычисление')
    def entering_numbers(self) -> None:
        """
        Эта функция вводит пример 7+8.
        """
        self.driver.find_element(By.XPATH, '//span[text() = "7"]').click()
        self.driver.find_element(By.XPATH, '//span[text() = "+"]').click()
        self.driver.find_element(By.XPATH, '//span[text() = "8"]').click()

    @allure.step('Кликнуть на =. Результат появляется через указанное время')
    def result(self) -> bool:
        """
        Эта функция кликает на = и ждет 45 секунд.
        Результат должен появиться через указанное время.

        При вводе другого времени ожидания в функции change_expectation,
        необходимо изменить время ожидания в переменной answer
        """
        self.driver.find_element(By.XPATH, '//span[text() = "="]').click()
        answer = WebDriverWait(self.driver, 45).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'screen'), '15'))
        return answer
