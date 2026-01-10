from selenium.webdriver.common.by import By


class Main:
    def __init__(self, browser):
        self.driver = browser
        self.driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
        self.driver.implicitly_wait(5)

    def filling_out_form(self, first_name, last_name, address, e_mail, phone, zip_code, city, country, job_position, company):
        self.driver.find_element(By.CSS_SELECTOR, '[name="first-name"]').send_keys(first_name)
        self.driver.find_element(By.CSS_SELECTOR, '[name="last-name"]').send_keys(last_name)
        self.driver.find_element(By.CSS_SELECTOR, '[name="address"]').send_keys(address)
        self.driver.find_element(By.CSS_SELECTOR, '[name="e-mail"]').send_keys(e_mail)
        self.driver.find_element(By.CSS_SELECTOR, '[name="phone"]').send_keys(phone)
        self.driver.find_element(By.CSS_SELECTOR, '[name="zip-code"]').send_keys(zip_code)
        self.driver.find_element(By.CSS_SELECTOR, '[name="city"]').send_keys(city)
        self.driver.find_element(By.CSS_SELECTOR, '[name="country"]').send_keys(country)
        self.driver.find_element(By.CSS_SELECTOR, '[name="job-position"]').send_keys(job_position)
        self.driver.find_element(By.CSS_SELECTOR, '[name="company"]').send_keys(company)

    def submit_form(self):
        self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    def zip_code_error(self):
        zip_code_return = self.driver.find_element(By.CSS_SELECTOR, '#zip-code').value_of_css_property('background-color')
        return zip_code_return

    def fields_success(self):
        for success in ['#first-name', '#last-name', '#address', '#e-mail', '#phone', '#city',
                        '#country', '#job-position', '#company']:
            green = self.driver.find_element(By.CSS_SELECTOR, success).value_of_css_property('background-color')
            return green
