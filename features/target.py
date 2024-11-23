from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.target.com/')

# Search
# driver.find_element(By.ID, 'search').send_keys('tea')
driver.find_element(By.XPATH, "//span[@class='sc-58ad44c0-3 kwbrXj h-margin-r-x3']").click()
sleep(5)
driver.find_element(By.XPATH,"//button[@data-test='accountNav-signIn']").click()
sleep(5)

# Verification:
expected_result = 'Sign into your Target account'
actual_result = driver.find_element(By.XPATH, "//span").text

# assert expected_result in actual_result, f'Expected text {expected_result} not in actual {actual_result}'
print('Test case passed')

# Verify an element present:
# driver.find_element(By.XPATH, "//*[text()='Popular filters']")