from selenium.webdriver.common.by import By
import allure

class Catalog:
    """
    Этот класс представляет страницу с каталогом товаров
    """
    def __init__(self, browser):
        self.driver = browser
        self.driver.implicitly_wait(10)

    @allure.step('Добавить товары в корзину: Sauce Labs Backpack, '
                 'Sauce Labs Bolt T-Shirt, Sauce Labs Onesie.'
                 'Кликнуть на значок корзины')
    def adding_product_to_cart(self) -> None:
        """
        Эта функция добавляет указанные товары в корзину и переходит в нее
        """
        self.driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
        self.driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
        self.driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()
        self.driver.find_element(By.CSS_SELECTOR, 'a.shopping_cart_link').click()

    @allure.step('Кликнуть на кнопку checkout')
    def cart(self) -> None:
        """
        Эта функция кликает на кнопку checkout, чтобы перейти к доставке
        """
        self.driver.find_element(By.CSS_SELECTOR, '#checkout').click()
