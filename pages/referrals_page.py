from selenium.webdriver.common.by import By
from pages.base_page import Page


class Referrals(Page):
    # NOTE: I am not including Header and Footer here, they should be separate Page Objects

    INVITE_FRIENDS_BTN = (By.XPATH, "//a[@class = 'btn-orange-round' and contains(@href, '/invite')]")
    REFER_FRIENDS_IMG = (By.XPATH, "//img[contains(@alt, 'Refer friends')]")
    INVITE_FRIENDS_HEADER = (By.CSS_SELECTOR, 'div.justify-content-center h1')
    INVITE_FRIENDS_CONTENT = (By.CSS_SELECTOR, 'div.justify-content-center p')

    # NOTE: Copy can be put into a separate file, keeping here for demo purposes only
    header_copy = 'Invite Friends & Earn'
    content_center_copy = "Some say it is better to give than to receive, but we believe it is even better to give and " \
                          "receive! If you refer someone to Fetch Rewards and they use your unique referral code when " \
                          "they sign up, you'll BOTH get 2,000 bonus points when they complete their first receipt. " \
                          "That's a win-win for everyone."


    def click_invite_friends_btn(self):
        self.wait_for_element_to_be_clickable(*self.INVITE_FRIENDS_BTN)
        self.click(*self.INVITE_FRIENDS_BTN)

    def open_referrals_page(self):
        self.open_page('referrals')

    def verify_referrals_page_opened(self):
        self.verify_page_opened('referrals')

    def verify_refer_friends_image_present(self):
        self.wait_for_element_appear(*self.REFER_FRIENDS_IMG)

    def verify_invite_friends_header_copy(self):
        self.verify_text(self.header_copy, *self.INVITE_FRIENDS_HEADER)

    def verify_invite_friends_content_copy(self):
        self.verify_text(self.content_center_copy, *self.INVITE_FRIENDS_CONTENT)
