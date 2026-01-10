from selenium.webdriver.common.by import By


class Cart:
    def __init__(self, browser):
        self.driver = browser
        self.driver.implicitly_wait(10)

    def user_data(self, first_name, last_name, postal_code):
        self.driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys(first_name)
        self.driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys(last_name)
        self.driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys(postal_code)
        self.driver.find_element(By.CSS_SELECTOR, '#continue').click()
