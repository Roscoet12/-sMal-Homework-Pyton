from selenium.webdriver.common.by import By


class Main:
    """
    Этот класс представляет страницу с формой для заполнения.
    У формы есть поля: Имя, Фамилия, Адрес, E-mail, телефон,
    зип-номер, город, страна, должность, компания.
    """
    def __init__(self, browser):
        self.driver = browser
        self.driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
        self.driver.implicitly_wait(5)

    def filling_out_form(self, first_name: str, last_name: str, address: str, e_mail: str, phone: str,
                         zip_code: str, city: str, country: str, job_position: str, company: str) -> None:
        """
        Эта функция заполняет данными форму.
        Принимаемые данные: Имя, Фамилия, Адрес, E-mail, телефон, зип-номер, город, страна, должность, компания.
        """
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

    def submit_form(self) -> None:
        """
        Эта функция нажимает на кнопку 'Submit', что отправляет заполненную форму.
        """
        self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    def zip_code_error(self) -> str:
        """
        Эта функция проверяет, что незаполненное поле 'Зип-код' подсвечивается красным цветом.
        Возвращает rgba с кодом цвета.
        """
        zip_code_return = self.driver.find_element(By.CSS_SELECTOR, '#zip-code').value_of_css_property('background-color')
        return zip_code_return

    def fields_success(self) -> str:
        """
        Эта функция проверяет, что остальные заполненные поля - Имя, Фамилия, Адрес,
        E-mail, Телефон, Город, Страна, Должность, Компания, подсвечиваются зеленым цветом.
        Возвращает rgba с кодом цвета.
        """
        for success in ['#first-name', '#last-name', '#address', '#e-mail', '#phone', '#city',
                        '#country', '#job-position', '#company']:
            green = self.driver.find_element(By.CSS_SELECTOR, success).value_of_css_property('background-color')
            return green
