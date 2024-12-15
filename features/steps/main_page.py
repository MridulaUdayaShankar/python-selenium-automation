from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_main_page(context):
    context.driver.get("https://www.target.com")


@when('Click on cart icon')
def click_cart(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='@web/CartLink']").click()
    sleep(3)


@when('Click Sign in')
def click_sign_in(context):
        context.driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()
        sleep(3)


@when('From right side navigation menu, click Sign in')
def click_right_side_nav_sign_in(context):
        context.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
