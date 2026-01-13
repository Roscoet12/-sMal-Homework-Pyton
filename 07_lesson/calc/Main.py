from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Main:
    def __init__(self, browser):
        self.driver = browser

    def get_browser(self):
        self.driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

    def change_expectation(self, expectation):
        self.driver.find_element(By.CSS_SELECTOR, '#delay').clear()
        self.driver.find_element(By.CSS_SELECTOR, '#delay').send_keys(expectation)

    def entering_numbers(self):
        self.driver.find_element(By.XPATH, '//span[text() = "7"]').click()
        self.driver.find_element(By.XPATH, '//span[text() = "+"]').click()
        self.driver.find_element(By.XPATH, '//span[text() = "8"]').click()

    def result(self):
        self.driver.find_element(By.XPATH, '//span[text() = "="]').click()
        answer = WebDriverWait(self.driver, 45).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'screen'), '15'))
        return answer
