from selenium.webdriver.common.by import By
from pages.base_page import Page

class Footer(Page):
    ABOUT_US_LINK = (By.XPATH, "//a[@href='/aboutUs.jsp']")
    OPEN_POSITIONS_LINK = (By.XPATH, "//a[text()='Open Positions']")

    def click_about_us_link(self):
        self.wait_for_element_to_be_clickable(*self.ABOUT_US_LINK)
        self.click(*self.ABOUT_US_LINK)

    def click_open_positions_link(self):
        self.wait_for_element_to_be_clickable(*self.OPEN_POSITIONS_LINK)
        self.click(*self.OPEN_POSITIONS_LINK)