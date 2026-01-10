from selenium.webdriver.common.by import By


class Main:
    def __init__(self, browser):
        self.driver = browser
        self.driver.implicitly_wait(10)

    def get_browser(self):
        self.driver.get('https://www.saucedemo.com/')

    def autorization(self, user_name, password):
        self.driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys(user_name)
        self.driver.find_element(By.CSS_SELECTOR, '#password').send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, '#login-button').click()
