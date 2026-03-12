import unittest
import time
import random
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from pages.porsche_page import PorschePage
from pages.porsche_firefox_page import PorscheFirefoxPage
import HtmlTestRunner



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

        self.assertEqual(driver.title, "Porsche 718 Cayman | Porsche International")
        delay()

    def test_TC_P_02(self):
        driver = self.driver
        page = PorschePage(driver)

        page.open()
        delay()
        page.accept_cookies_with_tab()

        caymen = driver.find_element(By.XPATH, "//h1[normalize-space()='718 Cayman']")
        self.assertTrue(caymen.is_displayed())

        roadster_button = driver.find_element(By.XPATH, "//a[normalize-space()='Roadster']")
        driver.execute_script("arguments[0].click();", roadster_button)
        time.sleep(4)

        self.assertEqual(driver.title, "Porsche 718 Boxster | Porsche International")
        delay()

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
        time.sleep(2)

        driver.back()
        time.sleep(2)

    def test_TC_P_04(self):
        driver = self.driver
        page = PorschePage(driver)

        page.open()
        delay()
        page.accept_cookies_with_tab()

        img = driver.find_element(By.XPATH,
                                  "//img[@alt='Porsche 718 Cayman in Jet Black Metallic in side view/in profile.']")
        self.assertTrue(img.is_displayed())

        txt = driver.find_element(By.XPATH,
                                  "//p[contains(text(),'The 718 models transfer the racing spirit of the l')]")
        self.assertTrue(txt.is_displayed())

        self.assertEqual(driver.title, "Porsche 718 Cayman | Porsche International")

    def test_TC_P_05(self):
        driver = self.driver
        page = PorschePage(driver)

        page.open()
        delay()
        page.accept_cookies_with_tab()

        button = driver.find_element(By.CSS_SELECTOR, "p-button[data-test='engine-sound-audio-controls_button']")
        driver.execute_script("arguments[0].scrollIntoView();", button)
        time.sleep(5)

        actions = ActionChains(driver)
        actions.click_and_hold(button).perform()
        self.assertTrue(button.is_displayed())
class FirefoxDriverPorsche(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.page_load_strategy = 'eager'
        options.add_argument("--disable-blink-features=AutomationControlled")
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_TC_P_01(self):
        driver = self.driver
        page = PorscheFirefoxPage(driver)

        page.open()
        page.accept_cookies()

        self.assertEqual(driver.title, "Porsche 718 Cayman | Porsche International")

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

        caymen = driver.find_element(By.XPATH, "//h1[normalize-space()='718 Cayman']")
        if caymen.is_displayed():
            print("Test passed")
        else:
            print("Test failed")
        time.sleep(4)
        roadster_button = driver.find_element(By.XPATH, "//a[normalize-space()='Roadster']")
        driver.execute_script("arguments[0].click();", roadster_button)
        # roadster_button.click()
        time.sleep(4)
        if driver.title == "Porsche 718 Boxster | Porsche International":
            print("Test passed")
        else:
            print("Test failed")


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

        # Назад
        driver.back()
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

        driver.find_element(By.XPATH,
                            "//img[@alt='Porsche 718 Cayman in Jet Black Metallic in side view/in profile.']").is_displayed()
        if driver.find_element(By.XPATH,
                               "//img[@alt='Porsche 718 Cayman in Jet Black Metallic in side view/in profile.']").is_displayed():
            print("Image is displayed")
        else:
            print("Test failed")
        delay()
        if driver.title == "Porsche 718 Cayman | Porsche International":
            print("Title is ok")
        else:
            print("Test failed")
        driver.find_element(By.XPATH,
                            "//p[contains(text(),'The 718 models transfer the racing spirit of the l')]").is_displayed()
        if driver.find_element(By.XPATH,
                               "//p[contains(text(),'The 718 models transfer the racing spirit of the l')]").is_displayed():
            print("Text is displayed")
        else:
            print("Test failed")


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
        button = driver.find_element(By.CSS_SELECTOR, "p-button[data-test='engine-sound-audio-controls_button']")
        driver.execute_script("arguments[0].scrollIntoView();", button)
        time.sleep(5)
        actions = ActionChains(driver)
        actions.click_and_hold(button).perform()
        if button.is_displayed():
            print("Button is displayed")
        else:
            print("Test failed")

class EdgeBrowser(unittest.TestCase):

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

        self.assertEqual(driver.title, "Porsche 718 Cayman | Porsche International")

    def test_TC_P_02(self):
        driver = self.driver
        page = PorschePage(driver)

        page.open()
        delay()
        page.accept_cookies_with_tab()

        caymen = driver.find_element(By.XPATH, "//h1[normalize-space()='718 Cayman']")
        self.assertTrue(caymen.is_displayed())

        roadster_button = driver.find_element(By.XPATH, "//a[normalize-space()='Roadster']")
        driver.execute_script("arguments[0].click();", roadster_button)
        time.sleep(4)

        self.assertEqual(driver.title, "Porsche 718 Boxster | Porsche International")

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
        time.sleep(2)

        driver.back()
        time.sleep(4)

    def test_TC_P_04(self):
        driver = self.driver
        page = PorschePage(driver)

        page.open()
        delay()
        page.accept_cookies_with_tab()

        img = driver.find_element(
            By.XPATH,
            "//img[@alt='Porsche 718 Cayman in Jet Black Metallic in side view/in profile.']"
        )
        self.assertTrue(img.is_displayed())

        txt = driver.find_element(
            By.XPATH,
            "//p[contains(text(),'The 718 models transfer the racing spirit of the l')]"
        )
        self.assertTrue(txt.is_displayed())

        self.assertEqual(driver.title, "Porsche 718 Cayman | Porsche International")
        delay()

    def test_TC_P_05(self):
        driver = self.driver
        page = PorschePage(driver)

        page.open()
        delay()
        page.accept_cookies_with_tab()

        button = driver.find_element(By.CSS_SELECTOR, "p-button[data-test='engine-sound-audio-controls_button']")
        driver.execute_script("arguments[0].scrollIntoView();", button)
        time.sleep(5)

        actions = ActionChains(driver)
        actions.click_and_hold(button).perform()
        self.assertTrue(button.is_displayed())



if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output='reports',
            report_title='Porsche Test Report',
            report_name='UI Tests'
        )
    )