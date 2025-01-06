from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

def search_product(context, product):
    print(product)
    context.driver.find_element(By.ID, 'search').send_keys('tea')
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(9)