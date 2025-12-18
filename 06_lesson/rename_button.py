from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('http://uitestingplayground.com/textinput')

new_name = driver.find_element(By.CSS_SELECTOR, '#newButtonName')
new_name.send_keys('SkyPro')
driver.find_element(By.CSS_SELECTOR, '#updatingButton').click()
button_text = driver.find_element(By.CSS_SELECTOR, '#updatingButton').text
print(button_text)

driver.quit()

