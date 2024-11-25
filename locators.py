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

driver.find_element(By.XPATH, "//select[@aria-label='Amazon']")
driver.find_element(By.ID, 'ap_email')
driver.find_element(By.ID, 'continue')

driver.find_element(By.XPATH, "//select[@class='legalTextRow' and @href = 'https://www.amazon.com/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&nodeId=508088']")
driver.find_element(By.XPATH, "//select[@class='legalTextRow' and @href = 'https://www.amazon.com/gp/help/customer/display.html/ref=ap_signin_notification_privacy_notice?ie=UTF8&nodeId=468496']")
driver.find_element(By.XPATH, "//select[@class= 'a-expander-prompt']")
driver.find_element(By.ID, 'auth-fpp-link-bottom')
driver.find_element(By.ID,'ap-other-signin-issues-link')

driver.find_element(By.ID,'createAccountSubmit')



