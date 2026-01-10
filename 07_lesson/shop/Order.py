from selenium.webdriver.common.by import By


class Order:
    def __init__(self, browser):
        self.driver = browser
        self.driver.implicitly_wait(10)

    def price(self):
        total = self.driver.find_element(By.CSS_SELECTOR, '.summary_total_label').text
        total = total.replace('Total: ', '')
        return total
