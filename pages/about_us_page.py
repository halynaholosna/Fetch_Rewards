from selenium.webdriver.common.by import By
from pages.base_page import Page


class AboutUs(Page):
    ABOUT_US_BTN = (By.XPATH, "//a[@class='btn-orange-round' and contains(text(), 'Jobs')]")

    def click_about_us_btn(self):
        self.click(*self.ABOUT_US_BTN)