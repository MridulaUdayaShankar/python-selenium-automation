from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SearchResultsPage(BasePage):
    SEARCH_RESULTS = (By.XPATH, "//div[@data-test='resultsHeading']")
    PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")

    def verify_search_results(self, product):
        # actual_result = self.find_element(*self.SEARCH_RESULTS).text
        # assert product in actual_result, f'Expected text {product} not in actual {actual_result}'
        self.verify_partial_text(product, *self.SEARCH_RESULTS)

    def verify_search_url(self, product):
            self.verify_partial_url(product)

    def get_product_name(self):
        return self.find_element(*self.PRODUCT_NAME).text