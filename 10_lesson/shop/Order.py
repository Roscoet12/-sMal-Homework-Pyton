from selenium.webdriver.common.by import By
import allure


class Order:
    """
    Этот класс представляет страницу обзора оформленного заказа и указанными данными для доставки
    """
    def __init__(self, browser):
        self.driver = browser
        self.driver.implicitly_wait(10)

    @allure.step('Найти фактическую цену заказа')
    def price(self) -> str:
        """"
         Эта функция находит полученную цену и возвращает ее
         """
        total = self.driver.find_element(By.CSS_SELECTOR, '.summary_total_label').text
        total = total.replace('Total: ', '')
        return total
