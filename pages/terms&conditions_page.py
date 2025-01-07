from pages.base_page import BasePage


class TermsAndConditionsPage(BasePage):

    def verify_pp_opened(self):
        self.verify_partial_url('target-terms-and-conditions-page/')