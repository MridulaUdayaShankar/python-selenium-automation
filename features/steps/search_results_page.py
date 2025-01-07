from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep
#from time import sleep


@then('Verify that correct search results shown for {product}')
def verify_results(context, product):
    # actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    # assert product in actual_result, f'Expected {product}, got actual {actual_result}'
    context.app.search_results_page.verify_search_results(product)

ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
ADD_TO_CART_BTN_SIDE_NAV = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")

LISTINGS = (By.CSS_SELECTOR, "[data-test*='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
PRODUCT_IMG = (By.CSS_SELECTOR, 'img')

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
    context.product_name = context.app.search_results_page.get_product_name()
    print(f'Product stored: {context.product_name}')


@when('Confirm Add to Cart button from side navigation')
def side_nav_click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN_SIDE_NAV).click()
    sleep(3)
    context.driver.wait.until(
        EC.element_to_be_clickable(ADD_TO_CART_BTN_SIDE_NAV),
        message='add to cart button not clickable'
    )

@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    # To see ALL listings (comment out if you only check top ones):
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    sleep(4)
    context.driver.execute_script("window.scrollBy(0,2000)", "")

    all_products = context.driver.find_elements(*LISTINGS)
    # print(all_products)
    assert len(all_products) > 0, 'No products found'

    for product in all_products:
        title = product.find_element(*PRODUCT_TITLE).text
        assert title != '', 'Product title not shown'
        # print(title)
        product.find_element(*PRODUCT_IMG)


@then('Verify search term {product} in URL')
def verify_search_url(context, product):
    context.app.search_results_page.verify_search_url(product)
