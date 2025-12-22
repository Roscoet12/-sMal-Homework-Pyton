from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calc():
    from selenium.webdriver.chrome.service import Service as ChromeService
    from webdriver_manager.chrome import ChromeDriverManager
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    try:
        driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

        driver.find_element(By.CSS_SELECTOR, '#delay').clear()
        driver.find_element(By.CSS_SELECTOR, '#delay').send_keys('45')

        driver.find_element(By.XPATH, '//span[text() = "7"]').click()
        driver.find_element(By.XPATH, '//span[text() = "+"]').click()
        driver.find_element(By.XPATH, '//span[text() = "8"]').click()
        driver.find_element(By.XPATH, '//span[text() = "="]').click()

        answer = WebDriverWait(driver, 45).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'screen'), '15'))
        assert answer == True

    finally:
        driver.quit()
