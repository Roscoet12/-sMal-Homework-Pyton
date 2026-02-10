from selenium import webdriver
import allure
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from calc.Main import Main

@allure.title('Подсчет результата через n времени ожидания')
@allure.description('Тест проверяет, что калькулятор выдает корректный результат через '
                    'указанное время. ')
@allure.feature('WAIT')
@allure.severity('CRITICAL')
def test_slow_calculator():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    main_pages = Main(browser)

    main_pages.get_browser()

    main_pages.change_expectation(45)

    main_pages.entering_numbers()

    result = main_pages.result()

    with allure.step('Проверить, что результат появился через указанное время'):
        assert result == True

    with allure.step('Закрыть браузер'):
        browser.quit()
