from selenium.webdriver.common.by import By

from pages.base_page import Base_Page


class SearchResultsPage(Base_Page):
    SEARCH_RESULTS = (By.XPATH, "//div[@data-test='resultsHeading']")

    def verify_search_results(self, product):
        actual_result = self.find_element(*self.SEARCH_RESULTS).text
        assert product in actual_result, f'Expected text {product} not in actual {actual_result}'