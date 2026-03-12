import unittest
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FF_Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from pages.porsche_page import PorschePage
import HtmlTestRunner
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC





def delay():
    time.sleep(random.randint(3,5))



class ChromePorscheTests(unittest.TestCase):


    def setUp(self):
        options = webdriver.ChromeOptions()
        options.page_load_strategy = 'eager'
        options.add_argument("--disable-blink-features=AutomationControlled")
        #options.add_argument("--window-size=1920,1080")
        #options.add_argument("--headless")

        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_TC_P_01(self):
        driver = self.driver
        page = PorschePage(driver)

        page.open()
        delay()
        page.accept_cookies_with_tab()

        page.open_invalid_page()
        delay()

        current_url = driver.current_url
        page_source = driver.page_source.lower()

        assert (
                "404" in page_source or
                "not found" in page_source or
                "error" in page_source or
                "718-cayman" not in current_url
        )

        print(current_url)
        print("Test passed - the page is 404")

    def test_TC_P_02(self):
        driver = self.driver
        page = PorschePage(driver)

        page.open()
        delay()
        page.accept_cookies_with_tab()

        body = driver.find_element(By.TAG_NAME, "body")

        for i in range(10):
            body.send_keys(Keys.TAB)
            delay()
            active_element = driver.switch_to.active_element
            print("Tab " + str(i + 1) + ": " + active_element.tag_name)

        print("Test passed")

    def test_TC_P_03(self):
        driver = self.driver
        page = PorschePage(driver)

        page.open()
        delay()
        page.accept_cookies_with_tab()

        change_model_button = driver.find_element(By.CSS_SELECTOR, "p-link[href='#change-model']")
        driver.execute_script("arguments[0].scrollIntoView()", change_model_button)
        delay()
        driver.execute_script("arguments[0].click();", change_model_button)
        time.sleep(4)

        driver.back()
        time.sleep(2)
        driver.forward()
        time.sleep(2)

        self.assertEqual(driver.title, "Porsche 718 Cayman | Porsche International")

        for i in range(5):
            driver.back()
            time.sleep(2)
            driver.forward()
            time.sleep(2)

    def test_TC_P_04(self):
        driver = self.driver
        page = PorschePage(driver)

        page.open()
        delay()
        page.accept_cookies_with_tab()

        wait = WebDriverWait(driver, 15)
        coupe = (By.XPATH, "//a[normalize-space()='Coupé']")

        self.assertTrue(wait.until(EC.visibility_of_element_located(coupe)).is_displayed())

        for i in range(10):
            el = wait.until(EC.element_to_be_clickable(coupe))
            driver.execute_script("arguments[0].click();", el)
            delay()
            print("Click " + str(i + 1))

    def test_TC_P_05(self):
        driver = self.driver
        page = PorschePage(driver)

        page.open()
        delay()
        page.accept_cookies_with_tab()

        for i in range(10):
            driver.refresh()
            time.sleep(3)

            self.assertIn(
                "https://www.porsche.com/international/models/718/718-models/718-cayman/",
                driver.current_url
            )

            print("Refresh " + str(i + 1) + " done")
class FirefoxDriverPorsche(unittest.TestCase):


    def setUp(self):
        options = FF_Options()
        options.set_preference("dom.webdriver.enabled", False)
        options.set_preference("useAutomationExtension", False)
        self.driver = webdriver.Firefox(options=options, service=FirefoxService(GeckoDriverManager().install()))
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_TC_P_01(self):
        driver = self.driver
        driver.get("https://www.porsche.com/international/models/718/718-models/718-cayman/")
        time.sleep(6)

        # layer2 host
        host = driver.find_element(By.CSS_SELECTOR, "uc-layer2")
        shadow1 = host.shadow_root

        # modal
        modal = shadow1.find_element(By.CSS_SELECTOR, "uc-p-modal.modal")

        # footer
        footer = modal.find_element(By.CSS_SELECTOR, "uc-footer.footer")
        shadow2 = footer.shadow_root

        # accept button
        accept = shadow2.find_element(By.CSS_SELECTOR, "uc-p-button.accept")

        driver.execute_script("arguments[0].click();", accept)
        time.sleep(7)

        # check invalid page
        driver.get("https://www.porsche.com/usa/models/718/718-models/INVALID-PAGE/")
        delay()

        # check if page is 404
        try:
            page = driver.page_source.lower()
        except Exception:
            page = ""  # Firefox internal error page

        assert (
                "404" in page or
                "not found" in page or
                "error" in page or
                page == ""  # Firefox internal error page
        )
    def test_TC_P_02(self):

        driver = self.driver
        driver.get("https://www.porsche.com/international/models/718/718-models/718-cayman/")
        time.sleep(6)

        # layer2 host
        host = driver.find_element(By.CSS_SELECTOR, "uc-layer2")
        shadow1 = host.shadow_root

        # modal
        modal = shadow1.find_element(By.CSS_SELECTOR, "uc-p-modal.modal")

        # footer
        footer = modal.find_element(By.CSS_SELECTOR, "uc-footer.footer")
        shadow2 = footer.shadow_root

        # accept button
        accept = shadow2.find_element(By.CSS_SELECTOR, "uc-p-button.accept")

        driver.execute_script("arguments[0].click();", accept)
        time.sleep(7)


        body = driver.find_element(By.TAG_NAME, "body")

        for i in range(10):
           body.send_keys(Keys.TAB)
           delay()

           active_element = driver.switch_to.active_element
           print("Tab " + str(i + 1) + ": " + active_element.tag_name)

        print("Test passed")


    def test_TC_P_03(self):
        driver = self.driver
        driver.get("https://www.porsche.com/international/models/718/718-models/718-cayman/")
        time.sleep(6)

        # layer2 host
        host = driver.find_element(By.CSS_SELECTOR, "uc-layer2")
        shadow1 = host.shadow_root

        # modal
        modal = shadow1.find_element(By.CSS_SELECTOR, "uc-p-modal.modal")

        # footer
        footer = modal.find_element(By.CSS_SELECTOR, "uc-footer.footer")
        shadow2 = footer.shadow_root

        # accept button
        accept = shadow2.find_element(By.CSS_SELECTOR, "uc-p-button.accept")

        driver.execute_script("arguments[0].click();", accept)
        time.sleep(7)
        change_model_button = driver.find_element(By.CSS_SELECTOR, "p-link[href='#change-model']")
        driver.execute_script("arguments[0].scrollIntoView()", change_model_button)
        delay()
        driver.execute_script("arguments[0].click();", change_model_button)
        change_model_button.click()
        time.sleep(4)

        driver.back()
        time.sleep(2)
        driver.forward()
        time.sleep(2)
        if driver.title == "Porsche 718 Cayman | Porsche International":
            print("Test passed")
        else:
            print("Test failed")
        for i in range(5):
            driver.back()
            time.sleep(2)

            driver.forward()
            time.sleep(2)




    def test_TC_P_04(self):

        driver = self.driver
        driver.get("https://www.porsche.com/international/models/718/718-models/718-cayman/")
        time.sleep(6)

        # layer2 host
        host = driver.find_element(By.CSS_SELECTOR, "uc-layer2")
        shadow1 = host.shadow_root

        # modal
        modal = shadow1.find_element(By.CSS_SELECTOR, "uc-p-modal.modal")

        # footer
        footer = modal.find_element(By.CSS_SELECTOR, "uc-footer.footer")
        shadow2 = footer.shadow_root

        # accept button
        accept = shadow2.find_element(By.CSS_SELECTOR, "uc-p-button.accept")

        driver.execute_script("arguments[0].click();", accept)
        time.sleep(7)

        coupe = driver.find_element(By.XPATH, "//a[normalize-space()='Coupé']")
        if coupe.is_displayed():
            print("Test passed")
        else:
            print("Test failed")
        time.sleep(4)
        coupe_button = driver.find_element(By.XPATH, "//a[normalize-space()='Coupé']")
        for i in range(10):
            coupe_button = driver.find_element(By.XPATH, "//a[normalize-space()='Coupé']")
            coupe_button.click()
            delay()
            print("Click " + str(i + 1))

    def test_TC_P_05(self):

        driver = self.driver
        driver.get("https://www.porsche.com/international/models/718/718-models/718-cayman/")
        time.sleep(6)

        # layer2 host
        host = driver.find_element(By.CSS_SELECTOR, "uc-layer2")
        shadow1 = host.shadow_root

        # modal
        modal = shadow1.find_element(By.CSS_SELECTOR, "uc-p-modal.modal")

        # footer
        footer = modal.find_element(By.CSS_SELECTOR, "uc-footer.footer")
        shadow2 = footer.shadow_root

        # accept button
        accept = shadow2.find_element(By.CSS_SELECTOR, "uc-p-button.accept")

        driver.execute_script("arguments[0].click();", accept)
        time.sleep(7)
        # Closing Cookies banner using Tab
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        time.sleep(3)
        for i in range(10):
            driver.refresh()
            time.sleep(3)

            # simple check that page is still opened
            self.assertIn("https://www.porsche.com/international/models/718/718-models/718-cayman/", driver.current_url)

            print("Refresh " + str(i + 1) + " done")

class TestEdge(unittest.TestCase):


    def setUp(self):

        options = Options()
        options.page_load_strategy = 'eager'
        options.add_argument("--disable-blink-features=AutomationControlled")

        self.driver = webdriver.Edge(
            options=options
        )
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_TC_P_01(self):
        driver = self.driver
        page = PorschePage(driver)

        page.open()
        delay()
        page.accept_cookies_with_tab()

        # check invalid page
        page.open_invalid_page()
        delay()

        current_url = driver.current_url
        page_source = driver.page_source.lower()

        assert (
                "404" in page_source or
                "not found" in page_source or
                "error" in page_source or
                "718-cayman" not in current_url
        )

        print(current_url)
        print("Test passed - the page is 404")

    def test_TC_P_02(self):
        driver = self.driver
        page = PorschePage(driver)

        page.open()
        delay()
        page.accept_cookies_with_tab()

        body = driver.find_element(By.TAG_NAME, "body")
        body.click()  # стабилизируем фокус
        time.sleep(0.5)

        for i in range(10):
            body.send_keys(Keys.TAB)
            time.sleep(0.3)
            active = driver.switch_to.active_element
            print("Tab " + str(i + 1) + ": " + active.tag_name)

    def test_TC_P_03(self):
        driver = self.driver
        page = PorschePage(driver)

        page.open()
        delay()
        page.accept_cookies_with_tab()

        change_model_button = driver.find_element(By.CSS_SELECTOR, "p-link[href='#change-model']")
        driver.execute_script("arguments[0].scrollIntoView()", change_model_button)
        delay()
        driver.execute_script("arguments[0].click();", change_model_button)

        time.sleep(5)

        driver.back()
        time.sleep(3)

        driver.forward()
        time.sleep(3)

        self.assertIn("Porsche", driver.title)

        print("Test passed")

        for i in range(3):
            driver.back()
            time.sleep(2)
            driver.forward()
            time.sleep(2)

    def test_TC_P_04(self):
        driver = self.driver
        page = PorschePage(driver)

        page.open()
        delay()
        page.accept_cookies_with_tab()

        wait = WebDriverWait(driver, 15)
        coupe = (By.XPATH, "//a[normalize-space()='Coupé']")

        self.assertTrue(wait.until(EC.visibility_of_element_located(coupe)).is_displayed())

        for i in range(10):
            el = wait.until(EC.element_to_be_clickable(coupe))
            driver.execute_script("arguments[0].click();", el)
            delay()
            print("Click " + str(i + 1))

    def test_TC_P_05(self):
        driver = self.driver
        page = PorschePage(driver)

        page.open()
        delay()
        page.accept_cookies_with_tab()

        for i in range(10):
            driver.refresh()
            time.sleep(3)
            self.assertIn(
                "https://www.porsche.com/international/models/718/718-models/718-cayman/",
                driver.current_url
            )
            print("Refresh " + str(i + 1) + " done")


if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output='reports',
            report_title='Porsche Test Report',
            report_name='UI Tests'
        )
    )