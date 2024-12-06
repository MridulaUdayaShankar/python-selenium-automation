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


# Amazon logo
driver.find_element(By.CSS_SELECTOR, 'i.a-icon.a-icon-logo')
# Create account label
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')
#  Your name text input box
driver.find_element(By.CSS_SELECTOR, 'input.a-input-text.a-span12.auth-autofocus.auth-required-field.a-form-error')
# Email text input box
driver.find_element(By.CSS_SELECTOR, 'input.a-input-text.a-span12.a-spacing-micro.auth-required-field.auth-require-claim-validation.a-form-error')
# Password input box
driver.find_element(By.CSS_SELECTOR, 'input.a-input-text.a-span12.auth-required-field.auth-require-fields-match.auth-require-password-validation.a-form-error')
# Password min-length alert
driver.find_element(By.CSS_SELECTOR, 'div.a-alert-content')
# Re-enter password
driver.find_element(By.CSS_SELECTOR,'input.a-input-text.a-span12.auth-required-field.auth-require-fields-match')
# continue button
driver.find_element(By.CSS_SELECTOR,'input#continue')
# Conditions of use
driver.find_element(By.CSS_SELECTOR, "a[href='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088']")
# Privacy Notice
driver.find_element(By.CSS_SELECTOR, "a[href='/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice?ie=UTF8&nodeId=468496']")
# Sign-in
driver.find_element(By.CSS_SELECTOR,'a.a-link-emphasis')
