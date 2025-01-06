from pages.base_page import Base_Page


class MainPage(Base_Page):

    def open_main(self):
        self.open('https://www.target.com/')