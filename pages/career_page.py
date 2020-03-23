from selenium.webdriver.common.by import By
from pages.base_page import Page


class OpenPositions(Page):
    TOP_LINKS = (By.CSS_SELECTOR, "a.nav-link")
    TITLE_TEXT = (By.ID, "board_title")

    def verify_open_positions_title(self, expected_text: str):
        self.verify_text(expected_text, *self.TITLE_TEXT)