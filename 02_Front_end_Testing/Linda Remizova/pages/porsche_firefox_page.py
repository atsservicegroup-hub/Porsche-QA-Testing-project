import time
from selenium.webdriver.common.by import By


class PorscheFirefoxPage:
    URL = "https://www.porsche.com/international/models/718/718-models/718-cayman/"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)
        time.sleep(6)

    def accept_cookies(self):
        # layer2 host
        host = self.driver.find_element(By.CSS_SELECTOR, "uc-layer2")
        shadow1 = host.shadow_root

        # modal
        modal = shadow1.find_element(By.CSS_SELECTOR, "uc-p-modal.modal")

        # footer
        footer = modal.find_element(By.CSS_SELECTOR, "uc-footer.footer")
        shadow2 = footer.shadow_root

        # accept button
        accept = shadow2.find_element(By.CSS_SELECTOR, "uc-p-button.accept")
        self.driver.execute_script("arguments[0].click();", accept)

        time.sleep(2)