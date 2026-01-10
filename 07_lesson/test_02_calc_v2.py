from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from calc.Main import Main


def test_slow_calculator():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    main_pages = Main(browser)

    main_pages.get_browser()

    main_pages.change_expectation('45')

    main_pages.entering_numbers()

    result = main_pages.result()

    return result == True

    browser.quit()
