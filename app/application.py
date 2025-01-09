from pages.base_page import BasePage
from pages.cart_page import CartPage
from pages.header import Header
from pages.main_page import MainPage
from pages.sign_in_page import SignInPage
from pages.search_results_page import SearchResultsPage
from pages.privacy_policy import PrivacyPolicyPage
from pages.target_app_page import TargetAppPage


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.base_page = BasePage(driver)
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.sign_in_page = SignInPage(driver)
        self.cart_page = CartPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.privacy_policy_page = PrivacyPolicyPage(driver)
        self.target_app_page = TargetAppPage(driver)
