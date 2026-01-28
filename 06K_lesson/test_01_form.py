from selenium import webdriver
from selenium.webdriver.common.by import By


def test_color():
    from selenium.webdriver.edge.service import Service as EdgeService
    edge_path = EdgeService(r'C:\Users\Roscoe\Desktop\учеба тест\учеба тест\Pyton\msedgedriver.exe')
    driver = webdriver.Edge(service=edge_path)

    try:
        driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

        driver.find_element(By.CSS_SELECTOR, '[name="first-name"]').send_keys('Иван')
        driver.find_element(By.CSS_SELECTOR, '[name="last-name"]').send_keys('Петров')
        driver.find_element(By.CSS_SELECTOR, '[name="address"]').send_keys('Ленина, 55-3')
        driver.find_element(By.CSS_SELECTOR, '[name="e-mail"]').send_keys('test@skypro.com')
        driver.find_element(By.CSS_SELECTOR, '[name="phone"]').send_keys('+7985899998787')
        driver.find_element(By.CSS_SELECTOR, '[name="zip-code"]').send_keys('')
        driver.find_element(By.CSS_SELECTOR, '[name="city"]').send_keys('Москва')
        driver.find_element(By.CSS_SELECTOR, '[name="country"]').send_keys('Россия')
        driver.find_element(By.CSS_SELECTOR, '[name="job-position"]').send_keys('QA')
        driver.find_element(By.CSS_SELECTOR, '[name="company"]').send_keys('SkyPro')

        driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

        # Поле zip code подсвечено красным
        zip_code_field = driver.find_element(By.CSS_SELECTOR, '#zip-code')
        assert 'rgba(248, 215, 218, 1)' in zip_code_field.value_of_css_property('background-color')

        # Остальные поля подсвечены зеленым
        for success in ['#first-name', '#last-name', '#address', '#e-mail', '#phone', '#city',
                        '#country', '#job-position', '#company']:
            green = driver.find_element(By.CSS_SELECTOR, success)
            assert 'rgba(209, 231, 221, 1)' in green.value_of_css_property('background-color')

    finally:
        driver.quit()
