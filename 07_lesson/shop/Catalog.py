from selenium.webdriver.common.by import By


class Catalog:
    def __init__(self, browser):
        self.driver = browser
        self.driver.implicitly_wait(10)

    def adding_product_to_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
        self.driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
        self.driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()
        self.driver.find_element(By.CSS_SELECTOR, 'a.shopping_cart_link').click()

    def cart(self):
        self.driver.find_element(By.CSS_SELECTOR, '#checkout').click()
