import time
from selenium.webdriver.common.keys import Keys


class PorschePage:
    URL = "https://www.porsche.com/international/models/718/718-models/718-cayman/"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def accept_cookies_with_tab(self, tabs: int = 3, wait: float = 2.0):
        actions = (Keys.TAB * tabs) + Keys.ENTER
        self.driver.switch_to.active_element.send_keys(actions)
        time.sleep(wait)

    def open_invalid_page(self):
            self.driver.get("https://www.porsche.com/usa/models/718/718-models/INVALID-PAGE/")