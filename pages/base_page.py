from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://www.fetchrewards.com/'
        self.wait = WebDriverWait(self.driver, 5)

    def open_page(self, url: str=''):
        self.driver.get(self.base_url + url)

    def find_element(self, *locator):
        """
        :param locator: search strategy for find_element of a Web Element, ex. (By.ID, 'id')
        :return: WebElement
        """
        return self.driver.find_element(*locator)

    def click(self, *locator):
        """
        Clicks on WebElement
        :param locator: search strategy for find_element of a Web Element, ex. (By.ID, 'id')
        """
        self.driver.find_element(*locator).click()

    def verify_page_opened(self, url):
        self.wait.until(EC.url_contains(url=url))

    def verify_text(self, expected_text: str, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text == actual_text, f'Expected text {expected_text}, but got {actual_text}'

    def wait_for_element_to_be_clickable(self, *locator):
        self.driver.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_element_appear(self, *locator):
        self.driver.wait.until(EC.presence_of_element_located(locator))
