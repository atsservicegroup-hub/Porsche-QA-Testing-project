import unittest
from faker import Faker
import time as t
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from MilaS.helpers import element_helpers as h
fake = Faker()
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.remote.webdriver import WebDriver


class ChromePositiveTestCases(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.driver.execute_script("document.body.style.zoom='70%'")

    def test_1_incorrect_url(self):
        driver = self.driver
        driver.get("https://www.porsche.com/usa/?foo=bar&undefined_param=123&%ZZ=@@@&debug=true&null=&injection=<script>alert(1)</script>")
        WebDriverWait(driver, 5).until(EC.url_contains("porsche.com"))
        h.delay()
        print("\n--- Test 1: Verify that page is loading with invalid parameters added to url ")

        # Closing Cookies banner using Tab
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        t.sleep(3)

        is_visible = h.assert_elementXPATH_visible(
            driver,
            "//h1[normalize-space()='Access Denied']",
            description="Error message"
        )

        print("Test 1 Passed" if is_visible else "Test 1 Failed")

    def test_2_Small_resolution(self):
        driver = self.driver

        # Set window size BEFORE loading the page
        driver.set_window_size(320, 240)

        driver.get(h.url_main)

        WebDriverWait(driver, 10).until(EC.url_contains("porsche.com"))
        print("\n--- Test 2: Verify responsive layout of the page at extremely small resolutions ---")

        h.delay()

        # Close cookies banner
        try:
            cookie_btn = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
            )
            cookie_btn.click()
        except:
            pass

        h.assert_elementXPATH_visible(driver, "/html/body/phn-header", "logo")
        print("logo is visible")

    def test_3_typo_url(self):
        driver = self.driver
        driver.get("https://www.porsche.com/usasaa/")
        WebDriverWait(driver, 5).until(EC.url_contains("porsche.com"))
        h.delay()
        print("\n--- Test 3: Verify that company page is not loading with an incorrectly entered URL")

        # Closing Cookies banner using Tab
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        t.sleep(3)

        is_visible = h.assert_elementXPATH_visible(
            driver,
            "//div[@class='pcom-error-page-code']",
            description="Error message"
        )

        print("Test 3 Passed" if is_visible else "Test 3 Failed")

    def test_4_Large_Resolution(self):
        driver = self.driver

        # Set window size BEFORE loading the page
        driver.set_window_size(3840, 2160)

        driver.get(h.url_main)

        WebDriverWait(driver, 10).until(EC.url_contains("porsche.com"))
        print("\n--- Test 2: Verify responsive layout of the page at extremely large resolutions ---")

        h.delay()

        # Close cookies banner
        try:
            cookie_btn = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
            )
            cookie_btn.click()
        except:
            pass

        h.assert_elementXPATH_visible(driver, "/html/body/phn-header", "logo")
        print("logo is visible")


    def tearDown(self):
        self.driver.quit()

class EdgePositiveTestCases(unittest.TestCase):

    def setUp(self):
        options = webdriver.EdgeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")

        self.driver = webdriver.Edge(
            service=EdgeService(r"C:\webdriver\msedgedriver.exe"),
            options=options
        )
        self.driver.maximize_window()

    def test_1_incorrect_url(self):
        driver = self.driver
        driver.get(
            "https://www.porsche.com/usa/?foo=bar&undefined_param=123&%ZZ=@@@&debug=true&null=&injection=<script>alert(1)</script>")
        WebDriverWait(driver, 5).until(EC.url_contains("porsche.com"))
        h.delay()
        print("\n--- Test 1: Verify that page is loading with invalid parameters added to url ")

        # Closing Cookies banner using Tab
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        t.sleep(3)

        is_visible = h.assert_elementXPATH_visible(
            driver,
            "//h1[normalize-space()='Access Denied']",
            description="Error message"
        )

        print("Test 1 Passed" if is_visible else "Test 1 Failed")

    def test_2_Small_resolution(self):
        driver = self.driver

        # Set window size BEFORE loading the page
        driver.set_window_size(320, 240)

        driver.get(h.url_main)

        WebDriverWait(driver, 10).until(EC.url_contains("porsche.com"))
        print("\n--- Test 2: Verify responsive layout of the page at extremely small resolutions ---")

        h.delay()

        # Close cookies banner
        try:
            cookie_btn = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
            )
            cookie_btn.click()
        except:
            pass

        h.assert_elementXPATH_visible(driver, "/html/body/phn-header", "logo")
        print("logo is visible")

    def test_3_typo_url(self):
        driver = self.driver
        driver.get("https://www.porsche.com/usasaa/")
        WebDriverWait(driver, 5).until(EC.url_contains("porsche.com"))
        h.delay()
        print("\n--- Test 3: Verify that company page is not loading with an incorrectly entered URL")

        # Closing Cookies banner using Tab
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        t.sleep(3)

        is_visible = h.assert_elementXPATH_visible(
            driver,
            "//div[@class='pcom-error-page-code']",
            description="Error message"
        )

        print("Test 3 Passed" if is_visible else "Test 3 Failed")

    def test_4_Large_Resolution(self):
        driver = self.driver

        # Set window size BEFORE loading the page
        driver.set_window_size(3840, 2160)

        driver.get(h.url_main)

        WebDriverWait(driver, 10).until(EC.url_contains("porsche.com"))
        print("\n--- Test 2: Verify responsive layout of the page at extremely large resolutions ---")

        h.delay()

        # Close cookies banner
        try:
            cookie_btn = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
            )
            cookie_btn.click()
        except:
            pass

        h.assert_elementXPATH_visible(driver, "/html/body/phn-header", "logo")
        print("logo is visible")

    def tearDown(self):
        self.driver.quit()

class FirefoxDriverPorsche(unittest.TestCase):
    driver: WebDriver

    def setUp(self):
        self.driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install())
        )
        self.driver.maximize_window()

    def test_1_incorrect_url(self):
        driver = self.driver
        driver.get(
            "https://www.porsche.com/usa/?foo=bar&undefined_param=123&%ZZ=@@@&debug=true&null=&injection=<script>alert(1)</script>")
        WebDriverWait(driver, 5).until(EC.url_contains("porsche.com"))
        h.delay()
        print("\n--- Test 1: Verify that page is loading with invalid parameters added to url ")

        # Closing Cookies banner using Tab
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        t.sleep(3)

        is_visible = h.assert_elementXPATH_visible(
            driver,
            "//h1[normalize-space()='Access Denied']",
            description="Error message"
        )

        print("Test 1 Passed" if is_visible else "Test 1 Failed")

    def test_2_Small_resolution(self):
        driver = self.driver

        # Set window size BEFORE loading the page
        driver.set_window_size(320, 240)

        driver.get(h.url_main)

        WebDriverWait(driver, 10).until(EC.url_contains("porsche.com"))
        print("\n--- Test 2: Verify responsive layout of the page at extremely small resolutions ---")

        h.delay()

        # Close cookies banner
        try:
            cookie_btn = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
            )
            cookie_btn.click()
        except:
            pass

        h.assert_elementXPATH_visible(driver, "/html/body/phn-header", "logo")
        print("logo is visible")

    def test_3_typo_url(self):
        driver = self.driver
        driver.get("https://www.porsche.com/usasaa/")
        WebDriverWait(driver, 5).until(EC.url_contains("porsche.com"))
        h.delay()
        print("\n--- Test 3: Verify that company page is not loading with an incorrectly entered URL")

        # Closing Cookies banner using Tab
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        t.sleep(3)

        is_visible = h.assert_elementXPATH_visible(
            driver,
            "//div[@class='pcom-error-page-code']",
            description="Error message"
        )

        print("Test 3 Passed" if is_visible else "Test 3 Failed")

    def test_4_Large_Resolution(self):
        driver = self.driver

        # Set window size BEFORE loading the page
        driver.set_window_size(3840, 2160)

        driver.get(h.url_main)

        WebDriverWait(driver, 10).until(EC.url_contains("porsche.com"))
        print("\n--- Test 2: Verify responsive layout of the page at extremely large resolutions ---")

        h.delay()

        # Close cookies banner
        try:
            cookie_btn = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
            )
            cookie_btn.click()
        except:
            pass

        h.assert_elementXPATH_visible(driver, "/html/body/phn-header", "logo")
        print("logo is visible")

    def tearDown(self):
        # Close driver
        self.driver.quit()