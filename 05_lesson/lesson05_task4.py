from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get('http://the-internet.herokuapp.com/login')

username = driver.find_element(By.CSS_SELECTOR, '#username')
username.send_keys('tomsmith')

sleep(1)

password = driver.find_element(By.CSS_SELECTOR, '#password')
password.send_keys('SuperSecretPassword!')

sleep(1)

button = driver.find_element(By.CSS_SELECTOR, 'button.radius')
button.send_keys(Keys.RETURN)

sleep(3)

green_plate = driver.find_element(By.CSS_SELECTOR, '[id="flash-messages"]').text
print(green_plate)

driver.quit()
