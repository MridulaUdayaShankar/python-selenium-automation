from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def browser_init(context):

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)

    context.driver.wait = WebDriverWait(context.driver, timeout=10)

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)