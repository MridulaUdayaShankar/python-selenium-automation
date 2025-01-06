from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep
#from time import sleep


@then('Verify that correct search results shown for {product}')
def verify_results(context, product):
    actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert product in actual_result, f'Expected {product}, got actual {actual_result}'
    actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert product in actual_result, f'Expected {product}, got actual {actual_result}'


ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
ADD_TO_CART_BTN_SIDE_NAV = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")

CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")

@when('Click on Add to Cart button')
def click_add_to_cart(context):
    sleep(5)
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    sleep(3)
    context.driver.wait.until(
        EC.visibility_of_element_located(SIDE_NAV_PRODUCT_NAME),
        message='Side navigation product name not visible'
    )


@when('Store product name')
def store_product_name(context):
    context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    context.product_name = context.driver.find_element(*CART_ITEM_TITLE).text
    print(f'Product stored: {context.product_name}')


@when('Confirm Add to Cart button from side navigation')
def side_nav_click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN_SIDE_NAV).click()
    sleep(3)
    context.driver.wait.until(
        EC.element_to_be_clickable(ADD_TO_CART_BTN_SIDE_NAV),
        message='add to cart button not clickable'
    )