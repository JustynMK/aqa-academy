from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class BaseApp:

    def __init__(self, browser) -> None:
                sefl.browser = browser

    def navigate_to(self, url):
            self.browser.get(url)

    def wait_and_click(self, locator, timeout=15):
        #read what is implicit and explicit
        elem = self.browser.find_element(locator)
        