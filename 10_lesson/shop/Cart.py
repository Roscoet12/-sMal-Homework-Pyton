from selenium.webdriver.common.by import By
import allure


class Cart:
    """
    Этот класс представляет страницу с вводом данных для доставки
    """
    def __init__(self, browser):
        self.driver = browser
        self.driver.implicitly_wait(10)

    @allure.step('Ввести данные для доставки товаров валидными данными ')
    def user_data(self, first_name: str, last_name: str, postal_code: int) -> None:
        """
        Эта функция вводит в поля данные для доставки.
        Принимаемые данные - Имя, Фамилия, Почтовый индекс
        """
        self.driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys(first_name)
        self.driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys(last_name)
        self.driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys(postal_code)
        self.driver.find_element(By.CSS_SELECTOR, '#continue').click()
