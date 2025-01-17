from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")

@given('Open target main page')
def open_main(context):
    context.app.main_page.open_main()


@when('Click Sign in')
def click_sign_in(context):
    context.app.main_page.click_sign_in()

@when('From right side navigation menu, click Sign in')
def click_right_side_nav_sign_in(context):
    context.app.main_page.click_right_side_nav_sign_in()

def search_product(context, product):
    # context.driver.find_element(*SEARCH_FIELD).send_keys(product)
    # context.driver.find_element(*SEARCH_BTN).click()
    # sleep(10)
    context.app.header.search_product(product)

@when('Click on Cart icon')
def click_cart(context):
    # context.driver.find_element(*CART_ICON).click()
    context.app.header.click_cart()

@then('Verify at least 1 header link is shown')
def verify_header_links(context):
    el = context.driver.find_element(By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
    print('\nFind element:')
    print(el)


@then('Verify {expected_amount} header links are shown')
def verify_header_links_amount(context, expected_amount):
    links = context.driver.find_elements(By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
    print('\nFind elements:')
    print(links)
    print(type(len(links)))
    assert len(links) == int(expected_amount), f'Expected {expected_amount} links but got {len(links)}'