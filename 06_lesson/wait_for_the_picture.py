from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')
weiter = WebDriverWait(driver, 20)
for img in ['#compass', '#calendar', '#award', '#landscape']:
    weiter.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, img))
   )

img_three = driver.find_element(By.CSS_SELECTOR, '#award').get_attribute('src')
print(img_three)

driver.quit()
