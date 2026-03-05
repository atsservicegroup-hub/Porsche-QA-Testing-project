import unittest
import time
import random
import Helpers_P as HP
#import Helpers_N as HN
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


def delay():
    time.sleep(random.randint(2, 4))

# This function how to get inside the shadow DOM. Can be moved to helpers.
def get_shadow(driver, element):
    return driver.execute_script("return arguments[0].shadowRoot", element)


class ChromePorschePositiveTests(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.page_load_strategy = 'eager'
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--headless")

        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.driver.maximize_window()

    # This test is just closing banner "Accept cookies" though accessibility

    def test_TC_P_36(self):
        driver = self.driver
        print("Positive TC-036")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        HP.check_porsche_url(driver)

        # Finding the button Menu and click

        HP.finding_menu_button(driver)
        delay()

        # Finding Shopping Tools button and click

        HP.shopping_tools_button(driver)
        delay()

        print("Positive TC-036 PASS")

        driver.quit()

    def test_TC_P_37(self):
        driver = self.driver
        print("Positive TC-037")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        HP.check_porsche_url(driver)

        # Finding the button Menu and click

        HP.finding_menu_button(driver)
        delay()

        # Finding the button Shopping Tools and click

        HP.shopping_tools_button(driver)
        delay()

        # Finding Build Your Own button and click

        HP.build_your_own_button(driver)
        delay()

        # Check Build Your Own Url

        HP.check_build_your_own_url(driver)

        print("Positive TC-037 PASS")

        driver.quit()

    def test_TC_P_38(self):
        driver = self.driver
        print("Positive TC-038")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        HP.check_porsche_url(driver)

        # Finding the button Menu and click

        HP.finding_menu_button(driver)
        delay()

        # Finding the button Shopping Tools and click

        HP.shopping_tools_button(driver)
        delay()

        # Finding Compare Models button and click

        HP.compare_models_button(driver)
        delay()

        # Check Compare Models Url

        HP.check_compare_models_url(driver)

        print("Positive TC-038 PASS")

        driver.quit()

    def test_TC_P_39(self):
        driver = self.driver
        print("Positive TC-039")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        HP.check_porsche_url(driver)

        # Finding the button Menu and click

        HP.finding_menu_button(driver)
        delay()

        # Finding the button Shopping Tools and click

        HP.shopping_tools_button(driver)
        delay()

        # Finding New & Used Inventory button and click

        HP.new_and_used_button(driver)
        delay()

        # Check New & Used Inventory Url

        HP.check_new_and_used_url(driver)

        print("Positive TC-039 PASS")

        driver.quit()

    def test_TC_P_40(self):
        driver = self.driver
        print("Positive TC-040")
        driver.get("https://www.porsche.com/usa/")
        time.sleep(3)
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        HP.check_porsche_url(driver)

        # Finding the button Menu and click

        HP.finding_menu_button(driver)
        delay()

        # Finding the button Shopping Tools and click

        HP.shopping_tools_button(driver)
        delay()

        # Finding Current Vehicle Offers button and click

        HP.current_vehicle_offers_button(driver)
        delay()

        # Check Current Vehicle Offers Url

        HP.check_current_vehicle_offers_url(driver)

        print("Positive TC-040 PASS")

        driver.quit()

    def test_TC_P_41(self):
        driver = self.driver
        print("Positive TC-041")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        HP.check_porsche_url(driver)

        # Finding the button Menu and click

        HP.finding_menu_button(driver)
        delay()

        # Finding the button Shopping Tools and click

        HP.shopping_tools_button(driver)
        delay()

        # Finding Certified Pre-Owned & Warranty button and click

        HP.certified_button(driver)
        delay()

        # Check Certified Pre-Owned & Warranty Url

        HP.check_certified_url(driver)

        print("Positive TC-041 PASS")

        driver.quit()

    def test_TC_P_42(self):
        driver = self.driver
        print("Positive TC-042")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        HP.check_porsche_url(driver)

        # Finding the button Menu and click

        HP.finding_menu_button(driver)
        delay()

        # Finding the button Shopping Tools and click

        HP.shopping_tools_button(driver)
        delay()

        # Finding Porsche Financial Services button and click

        HP.porsche_financial_button(driver)
        delay()

        # Check Porsche Financial Services Url

        HP.check_porsche_financial_url(driver)

        print("Positive TC-042 PASS")

        driver.quit()

    def test_TC_P_43(self):
        driver = self.driver
        print("Positive TC-043")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        HP.check_porsche_url(driver)

        # Finding the button Menu and click

        HP.finding_menu_button(driver)
        delay()

        # Finding the button Shopping Tools and click

        HP.shopping_tools_button(driver)
        delay()

        # Finding E-Mobility & E-Performance button and click

        HP.e_mobility_button(driver)
        delay()

        # Check E-Mobility & E-Performance Url

        HP.check_e_mobility_url(driver)

        print("Positive TC-043 PASS")

        driver.quit()

    def test_TC_P_44(self):
        driver = self.driver
        print("Positive TC-044")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        HP.check_porsche_url(driver)

        # Finding the button Menu and click

        HP.finding_menu_button(driver)
        delay()

        # Finding Account button and click

        HP.account_button(driver)
        delay()

        # Finding Log In button and click

        HP.log_in_button(driver)
        delay()

        # Check Log In Url

        HP.check_log_in_url(driver)

        print("Positive TC-044 PASS")

        driver.quit()

    def test_TC_P_45(self):
        driver = self.driver
        print("Positive TC-045")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        HP.check_porsche_url(driver)

        # Finding the button Menu and click

        HP.finding_menu_button(driver)
        delay()

        # Finding Account button and click

        HP.account_button(driver)
        delay()

        # Finding Saved Searches button and click

        HP.saved_searches_button(driver)
        delay()

        # Check Saved Searches Url

        HP.check_saved_searches_url(driver)

        print("Positive TC-045 PASS")

        driver.quit()

    def test_TC_P_46(self):
        driver = self.driver
        print("Positive TC-046")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        HP.check_porsche_url(driver)

        # Finding the button Menu and click

        HP.finding_menu_button(driver)
        delay()

        # Finding Account button and click

        HP.account_button(driver)
        delay()

        # Finding Saved Cars button and click

        HP.saved_cars_button(driver)
        delay()

        # Check Saved Cars Url

        HP.check_saved_cars_url(driver)

        print("Positive TC-046 PASS")

        driver.quit()

    def test_TC_P_47(self):
        driver = self.driver
        print("Positive TC-047")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        HP.check_porsche_url(driver)

        # Finding the button Menu and click

        HP.finding_menu_button(driver)
        delay()

        # Finding Account button and click

        HP.account_button(driver)
        delay()

        # Finding Find Connect Services button and click

        HP.find_connect_services_button(driver)
        delay()

        # Check Find Connect Services Url

        HP.check_find_connect_services_url(driver)

        print("Positive TC-047 PASS")

        driver.quit()

    def test_TC_P_48(self):
        driver = self.driver
        print("Positive TC-048")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        HP.check_porsche_url(driver)

        # Finding the button Menu and click

        HP.finding_menu_button(driver)
        delay()

        # Finding Account button and click

        HP.account_button(driver)
        delay()

        # Finding Contact & Support button and click

        HP.contact_and_support_button(driver)
        delay()
        actions = Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Contact & Support Url

        HP.check_contact_and_support_url(driver)

        print("Positive TC-048 PASS")

        driver.quit()
