from pages.about_us_page import AboutUs
from pages.base_page import Page
from pages.footer import Footer
from pages.open_positions_page import OpenPositions
from pages.referrals_page import Referrals


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.about_us_page = AboutUs(self.driver)
        self.footer = Footer(self.driver)
        self.main_page = Page(self.driver)
        self.open_positions = OpenPositions(self.driver)
        self.referrals_page = Referrals(self.driver)
