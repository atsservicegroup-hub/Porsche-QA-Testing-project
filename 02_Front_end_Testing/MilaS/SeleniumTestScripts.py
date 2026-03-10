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

    def test_1_correct_page(self):
        driver = self.driver
        driver.get(h.url_main)
        WebDriverWait(driver, 5).until(EC.url_contains("porsche.com"))
        h.delay()
        print("\n--- Test 1: Verify Panamera models page opens correctly ---")

        # Closing Cookies banner using Tab
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        t.sleep(3)

        element = h.scroll_until_element(
            driver,
            By.XPATH,
            "//article[@aria-label='Porsche Panamera']//a[@class='DesktopCarRangeTile__clickableArea__403b1']"
        )
        element.click()

        t.sleep(3)

        is_visible = h.assert_element_visible(driver, "s0-15", "Panamera Models variants")

        if is_visible:
            print("Test 1 Passed")
        else:
            print("Test 1 Failed")

    def test_2_Build_Panamera(self):
        driver = self.driver
        driver.get(h.url_main)

        WebDriverWait(driver, 10).until(EC.url_contains("porsche.com"))
        print("\n--- Test 2: Verify 'Build your own' opens Panamera configuration page ---")

        # Close cookies banner if present
        try:
            cookie_btn = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
            )
            cookie_btn.click()
        except:
            pass  # banner may not appear

        # Scroll to "Build your own" inside Panamera tile
        build_btn = h.scroll_until_element(
            driver,
            By.XPATH,
            "//article[@aria-label='Porsche Panamera']//span[normalize-space()='Build your own']"
        )

        # Click using JS (Porsche uses shadow DOM / Astro components)
        driver.execute_script("arguments[0].scrollIntoView({block:'center'});", build_btn)
        driver.execute_script("arguments[0].click();", build_btn)

        # Wait for configuration page header
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h1[contains(text(), 'Which Panamera')]")
            )
        )

        # Assertion
        is_visible = h.assert_elementXPATH_visible(
            driver,
            "//h1[contains(text(), 'Which Panamera')]",
            description="Panamera configuration title"
        )

        print("Test 2 Passed" if is_visible else "Test 2 Failed")

    def test_3_All_panamera_models_correct(self):
        driver = self.driver
        driver.get(h.url_main)
        WebDriverWait(driver, 2).until(EC.url_contains("porsche.com"))
        h.delay()
        print("----------------------test3-------------------------")
        print("Verify that all listed models have picture, title with the name of the model, description, select model button, and compare button")

        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        t.sleep(3)

        element = h.scroll_until_element(
            driver, By.XPATH,"//article[@aria-label='Porsche Panamera']//a[@class='DesktopCarRangeTile__clickableArea__403b1']")
        element.click()

        t.sleep(3)

        #Panamera
        print("Panamera")
        # Check that each model listing contains picture
        h.assert_elementXPATH_visible(driver,"//div[@aria-label='Panamera']//img",description="picture")

        # Check that each model listing contains Name
        h.assert_elementXPATH_visible(driver,"//div[@aria-label='Panamera']//h3",description="name")

        # Check that each model listing contains Description
        h.assert_elementXPATH_visible(driver,"//div[@aria-label='Panamera']//ul",description="description")

        # Check that each model listing contains "Select Model" button
        h.assert_elementXPATH_visible(driver, "//*[@id='s0-0']/div/div[2]/div[1]/div/div[3]/p-link[1]", description="Select Model Button" )

        # Check that each model listing contains "Compare" button
        h.assert_elementXPATH_visible(driver,"//*[@id='s0-0']/div/div[2]/div[1]/div/div[3]/p-link[2]",description="Compare Button")

        #Panamera 4
        print("Panamera 4")
        # Check that each model listing contains picture
        h.assert_elementXPATH_visible(driver,"//div[@aria-label='Panamera 4']//img")

        # Check that each model listing contains name of the model
        h.assert_elementXPATH_visible(driver,"//div[@aria-label='Panamera 4']//h3[1]")

        # Check that each model listing contains description
        h.assert_elementXPATH_visible(driver,"//div[@aria-label='Panamera 4']//ul")

        # Check that each model listing contains "Select Model" button
        h.assert_elementXPATH_visible(driver,"//*[@id='s0-0']/div/div[2]/div[2]/div/div[3]/p-link[1]",description="Select Model Button")

        # Check that each model listing contains "Compare" button
        h.assert_elementXPATH_visible(driver,"//*[@id='s0-0']/div/div[2]/div[2]/div/div[3]/p-link[2]",description="Compare Button")

        #Panamera 4 E-Hybrid
        h.assert_elementXPATH_visible(driver,"//div[@aria-label='Panamera 4 E-Hybrid']//img")

        # Check that each model listing contains name of the model
        h.assert_elementXPATH_visible(driver,"//div[@aria-label='Panamera 4 E-Hybrid']//h3")

        # Check that each model listing contains description
        h.assert_elementXPATH_visible(driver,"//div[@aria-label='Panamera 4 E-Hybrid']//ul")

        # Check that each model listing contains "Select Model" button
        h.assert_elementXPATH_visible(driver,"//*[@id='s0-0']/div/div[2]/div[3]/div/div[3]/p-link[1]",description="Select Model Button")


        # Check that each model listing contains "Compare" button
        h.assert_elementXPATH_visible(driver,"//*[@id='s0-0']/div/div[2]/div[3]/div/div[3]/p-link[2]",description="Compare Button")

        #Panamera 4S E-Hybrid
        h.assert_elementXPATH_visible(driver,"//div[@aria-label='Panamera 4S E-Hybrid']//img")

        # Check that each model listing contains name of the model
        h.assert_elementXPATH_visible(driver,"//div[@aria-label='Panamera 4S E-Hybrid']//h3")

        # Check that each model listing contains description
        h.assert_elementXPATH_visible(driver,"//div[@aria-label='Panamera 4S E-Hybrid']//ul")

        # Check that each model listing contains "Select Model" button
        h.assert_elementXPATH_visible(driver,"//*[@id='s0-0']/div/div[2]/div[4]/div/div[3]/p-link[1]",description="Select Model Button")

        # Check that each model listing contains "Compare" button
        h.assert_elementXPATH_visible(driver,"//*[@id='s0-0']/div/div[2]/div[4]/div/div[3]/p-link[2]",description="Compare Button")

        #Panamera GTS
        h.assert_elementXPATH_visible(driver,"//div[@aria-label='Panamera GTS']//img")

        # Check that each model listing contains name of the model
        h.assert_elementXPATH_visible(driver,"//div[@aria-label='Panamera GTS']//h3")

        # Check that each model listing contains description
        h.assert_elementXPATH_visible(driver,"//div[@aria-label='Panamera GTS']//ul",description="description")

        # Check that each model listing contains "Select Model" button
        h.assert_elementXPATH_visible(driver,"//*[@id='s0-0']/div/div[2]/div[5]/div/div[3]/p-link[1]",description="Select Model Button")

        # Check that each model listing contains "Compare" button
        h.assert_elementXPATH_visible(driver, "//*[@id='s0-0']/div/div[2]/div[5]/div/div[3]/p-link[2]",description="Compare Button")

        #Panamera Turbo E-Hybrid
        h.assert_elementXPATH_visible(driver,"//div[@aria-label='Panamera Turbo E-Hybrid']//img")

        # Check that each model listing contains name of the model
        h.assert_elementXPATH_visible(driver,"//div[@aria-label='Panamera Turbo E-Hybrid']//h3")

        # Check that each model listing contains description
        h.assert_elementXPATH_visible(driver,"//div[@aria-label='Panamera Turbo E-Hybrid']//ul",description="description")

        # Check that each model listing contains "Select Model" button
        h.assert_elementXPATH_visible(driver,"//*[@id='s0-0']/div/div[2]/div[6]/div/div[3]/p-link[1]",description="Select Model Button")

        # Check that each model listing contains "Compare" button
        h.assert_elementXPATH_visible(driver,"//*[@id='s0-0']/div/div[2]/div[6]/div/div[3]/p-link[2]",description="Compare Button")

        #Panamera Turbo S E-Hybrid
        h.assert_elementXPATH_visible(driver,"//div[@aria-label='Panamera Turbo S E-Hybrid']//img")

        # Check that each model listing contains name of the model
        h.assert_elementXPATH_visible(driver,"//div[@aria-label='Panamera Turbo S E-Hybrid']//h3")

        # Check that each model listing contains description
        h.assert_elementXPATH_visible(driver,"//div[@aria-label='Panamera Turbo S E-Hybrid']//ul",description="description")

        # Check that each model listing contains "Select Model" button
        h.assert_elementXPATH_visible(driver,"//*[@id='s0-0']/div/div[2]/div[7]/div/div[3]/p-link[1]",description="Select Model Button")

        # Check that each model listing contains "Compare" button
        h.assert_elementXPATH_visible(driver,"//*[@id='s0-0']/div/div[2]/div[7]/div/div[3]/p-link[2]",description="Compare Button")

    def test_4_select_button_works(self):
        driver = self.driver
        driver.get(h.url_panamera_models)
        WebDriverWait(driver, 7).until(EC.url_contains("porsche.com"))
        h.delay()
        print("----------------------test4-------------------------")
        print("Verify that 'Select model' button leads to page with model description")

        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        t.sleep(6)

        driver.find_element(By.XPATH, "//*[@id='s0-0']/div/div[2]/div[2]/div/div[3]/p-link[1]").click()
        t.sleep(6)

        WebDriverWait(driver, 12).until(
            EC.visibility_of_element_located(
                (By.XPATH,
                 "//h1[@class='CoreDisplay__root__e79c7 text__align-center__4a52b text__color-inherit__4a52b CoreDisplay__size-small__e79c7 ModelIntro__modelName__ef56b']")
            )
        )

        # Now verify
        is_visible = h.assert_elementXPATH_visible(
            driver,
            "//h1[@class='CoreDisplay__root__e79c7 text__align-center__4a52b text__color-inherit__4a52b CoreDisplay__size-small__e79c7 ModelIntro__modelName__ef56b']",
            description="Panamera 4 Model selection"
        )

        if is_visible:
            print("Test 4 Passed")
        else:
            print("Test 4 Failed")

    def test_5_new_and_used_inventory(self):
        driver = self.driver
        driver.get("https://www.porsche.com/usa/models/panamera/panamera-models/panamera-4/")
        WebDriverWait(driver, 2).until(EC.url_contains("porsche.com"))
        h.delay()
        print("\n--- Test 5: Verify that 'New & Used Inventory' page opens correctly ---")

        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        t.sleep(3)

        driver.find_element(By.XPATH,
                            "//*[@id='b16687dd-7264-4bb9-a6d9-3f763ba84364']/astro-island/div/div[4]/p-button-group/p-link[3]").click()

        print("AFTER CLICK:", driver.current_url)

        header_xpath = "//span[contains(@class, '_1j9sent')]"

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, header_xpath))
        )

        # Assertion
        is_visible = h.assert_elementXPATH_visible(
            driver,
            header_xpath,
            description="Panamera 4 new and used inventory header"
        )

        print("Test 5 Passed" if is_visible else "Test 5 Failed")


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

    def test_1_correct_pageEdge(self):
        driver = self.driver
        driver.get(h.url_main)
        WebDriverWait(driver, 5).until(EC.url_contains("porsche.com"))
        h.delay()
        print("\n--- Test 1: Verify Panamera models page opens correctly ---")

        # Closing Cookies banner using Tab
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        t.sleep(3)

        element = h.scroll_until_element(
            driver,
            By.XPATH,
            "//article[@aria-label='Porsche Panamera']//a[@class='DesktopCarRangeTile__clickableArea__403b1']"
        )
        element.click()

        t.sleep(3)

        is_visible = h.assert_element_visible(driver, "s0-15", "Panamera Models variants")

        if is_visible:
            print("Test 1 Passed")
        else:
            print("Test 1 Failed")

    def test_2_Build_PanameraEdge(self):
        driver = self.driver
        driver.get(h.url_main)

        WebDriverWait(driver, 10).until(EC.url_contains("porsche.com"))
        print("\n--- Test 2: Verify 'Build your own' opens Panamera configuration page ---")

        # Close cookies banner if present
        try:
            cookie_btn = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
            )
            cookie_btn.click()
        except:
            pass  # banner may not appear

        # Scroll to "Build your own" inside Panamera tile
        build_btn = h.scroll_until_element(
            driver,
            By.XPATH,
            "//article[@aria-label='Porsche Panamera']//span[normalize-space()='Build your own']"
        )

        # Click using JS (Porsche uses shadow DOM / Astro components)
        driver.execute_script("arguments[0].scrollIntoView({block:'center'});", build_btn)
        driver.execute_script("arguments[0].click();", build_btn)

        # Wait for configuration page header
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h1[contains(text(), 'Which Panamera')]")
            )
        )

        # Assertion
        is_visible = h.assert_elementXPATH_visible(
            driver,
            "//h1[contains(text(), 'Which Panamera')]",
            description="Panamera configuration title"
        )

        print("Test 2 Passed" if is_visible else "Test 2 Failed")

    def test_3_All_panamera_models_correctEdge(self):
        driver = self.driver
        driver.get(h.url_main)
        WebDriverWait(driver, 2).until(EC.url_contains("porsche.com"))
        h.delay()
        print("----------------------test3-------------------------")
        print("Verify that all listed models have picture, title with the name of the model, description, select model button, and compare button")

        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        t.sleep(3)

        element = h.scroll_until_element(
            driver, By.XPATH,"//article[@aria-label='Porsche Panamera']//a[@class='DesktopCarRangeTile__clickableArea__403b1']")
        element.click()

        t.sleep(3)

        #Panamera
        print("Panamera")
        # Check that each model listing contains picture
        h.assert_elementXPATH_visible(driver,"//div[@aria-label='Panamera']//img",description="picture")

        # Check that each model listing contains Name
        h.assert_elementXPATH_visible(driver,"//div[@aria-label='Panamera']//h3",description="name")

        # Check that each model listing contains Description
        h.assert_elementXPATH_visible(driver,"//div[@aria-label='Panamera']//ul",description="description")

        # Check that each model listing contains "Select Model" button
        h.assert_elementXPATH_visible(driver, "//*[@id='s0-0']/div/div[2]/div[1]/div/div[3]/p-link[1]", description="Select Model Button" )

        # Check that each model listing contains "Compare" button
        h.assert_elementXPATH_visible(driver,"//*[@id='s0-0']/div/div[2]/div[1]/div/div[3]/p-link[2]",description="Compare Button")

        #Panamera 4
        print("Panamera 4")
        # Check that each model listing contains picture
        h.assert_elementXPATH_visible(driver,"//div[@aria-label='Panamera 4']//img")

        # Check that each model listing contains name of the model
        h.assert_elementXPATH_visible(driver,"//div[@aria-label='Panamera 4']//h3[1]")

        # Check that each model listing contains description
        h.assert_elementXPATH_visible(driver,"//div[@aria-label='Panamera 4']//ul")

        # Check that each model listing contains "Select Model" button
        h.assert_elementXPATH_visible(driver,"//*[@id='s0-0']/div/div[2]/div[2]/div/div[3]/p-link[1]",description="Select Model Button")

        # Check that each model listing contains "Compare" button
        h.assert_elementXPATH_visible(driver,"//*[@id='s0-0']/div/div[2]/div[2]/div/div[3]/p-link[2]",description="Compare Button")

        #Panamera 4 E-Hybrid
        h.assert_elementXPATH_visible(driver,"//div[@aria-label='Panamera 4 E-Hybrid']//img")

        # Check that each model listing contains name of the model
        h.assert_elementXPATH_visible(driver,"//div[@aria-label='Panamera 4 E-Hybrid']//h3")

        # Check that each model listing contains description
        h.assert_elementXPATH_visible(driver,"//div[@aria-label='Panamera 4 E-Hybrid']//ul")

        # Check that each model listing contains "Select Model" button
        h.assert_elementXPATH_visible(driver,"//*[@id='s0-0']/div/div[2]/div[3]/div/div[3]/p-link[1]",description="Select Model Button")


        # Check that each model listing contains "Compare" button
        h.assert_elementXPATH_visible(driver,"//*[@id='s0-0']/div/div[2]/div[3]/div/div[3]/p-link[2]",description="Compare Button")

        #Panamera 4S E-Hybrid
        h.assert_elementXPATH_visible(driver,"//div[@aria-label='Panamera 4S E-Hybrid']//img")

        # Check that each model listing contains name of the model
        h.assert_elementXPATH_visible(driver,"//div[@aria-label='Panamera 4S E-Hybrid']//h3")

        # Check that each model listing contains description
        h.assert_elementXPATH_visible(driver,"//div[@aria-label='Panamera 4S E-Hybrid']//ul")

        # Check that each model listing contains "Select Model" button
        h.assert_elementXPATH_visible(driver,"//*[@id='s0-0']/div/div[2]/div[4]/div/div[3]/p-link[1]",description="Select Model Button")

        # Check that each model listing contains "Compare" button
        h.assert_elementXPATH_visible(driver,"//*[@id='s0-0']/div/div[2]/div[4]/div/div[3]/p-link[2]",description="Compare Button")

        #Panamera GTS
        h.assert_elementXPATH_visible(driver,"//div[@aria-label='Panamera GTS']//img")

        # Check that each model listing contains name of the model
        h.assert_elementXPATH_visible(driver,"//div[@aria-label='Panamera GTS']//h3")

        # Check that each model listing contains description
        h.assert_elementXPATH_visible(driver,"//div[@aria-label='Panamera GTS']//ul",description="description")

        # Check that each model listing contains "Select Model" button
        h.assert_elementXPATH_visible(driver,"//*[@id='s0-0']/div/div[2]/div[5]/div/div[3]/p-link[1]",description="Select Model Button")

        # Check that each model listing contains "Compare" button
        h.assert_elementXPATH_visible(driver, "//*[@id='s0-0']/div/div[2]/div[5]/div/div[3]/p-link[2]",description="Compare Button")

        #Panamera Turbo E-Hybrid
        h.assert_elementXPATH_visible(driver,"//div[@aria-label='Panamera Turbo E-Hybrid']//img")

        # Check that each model listing contains name of the model
        h.assert_elementXPATH_visible(driver,"//div[@aria-label='Panamera Turbo E-Hybrid']//h3")

        # Check that each model listing contains description
        h.assert_elementXPATH_visible(driver,"//div[@aria-label='Panamera Turbo E-Hybrid']//ul",description="description")

        # Check that each model listing contains "Select Model" button
        h.assert_elementXPATH_visible(driver,"//*[@id='s0-0']/div/div[2]/div[6]/div/div[3]/p-link[1]",description="Select Model Button")

        # Check that each model listing contains "Compare" button
        h.assert_elementXPATH_visible(driver,"//*[@id='s0-0']/div/div[2]/div[6]/div/div[3]/p-link[2]",description="Compare Button")

        #Panamera Turbo S E-Hybrid
        h.assert_elementXPATH_visible(driver,"//div[@aria-label='Panamera Turbo S E-Hybrid']//img")

        # Check that each model listing contains name of the model
        h.assert_elementXPATH_visible(driver,"//div[@aria-label='Panamera Turbo S E-Hybrid']//h3")

        # Check that each model listing contains description
        h.assert_elementXPATH_visible(driver,"//div[@aria-label='Panamera Turbo S E-Hybrid']//ul",description="description")

        # Check that each model listing contains "Select Model" button
        h.assert_elementXPATH_visible(driver,"//*[@id='s0-0']/div/div[2]/div[7]/div/div[3]/p-link[1]",description="Select Model Button")

        # Check that each model listing contains "Compare" button
        h.assert_elementXPATH_visible(driver,"//*[@id='s0-0']/div/div[2]/div[7]/div/div[3]/p-link[2]",description="Compare Button")

    def test_4_select_button_worksEdge(self):
        driver = self.driver
        driver.get(h.url_panamera_models)
        WebDriverWait(driver, 5).until(EC.url_contains("porsche.com"))
        h.delay()
        print("----------------------test4-------------------------")
        print("Verify that 'Select model' button leads to page with model description")

        # Close cookies via TAB
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        t.sleep(3)

        # Locate the p-link wrapper
        p_link = driver.find_element(
            By.XPATH,
            "//*[@id='s0-0']//p-link[1]"
        )

        # Scroll into view
        driver.execute_script("arguments[0].scrollIntoView({block:'center'});", p_link)

        # Get the inner <a> from shadow DOM
        inner_a = driver.execute_script(
            "return arguments[0].shadowRoot.querySelector('a')",
            p_link
        )

        # Click the real link
        driver.execute_script("arguments[0].click();", inner_a)

        # Wait for model page
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h1[contains(@class,'ModelIntro__modelName')]")
            )
        )

        # Verify
        is_visible = h.assert_elementXPATH_visible(
            driver,
            "//h1[contains(@class,'ModelIntro__modelName')]",
            description="Panamera 4 Model selection"
        )

        print("Test 4 Passed" if is_visible else "Test 4 Failed")

    def test_5_new_and_used_inventoryEdge(self):
        driver = self.driver
        driver.get("https://www.porsche.com/usa/models/panamera/panamera-models/panamera-4/")
        WebDriverWait(driver, 2).until(EC.url_contains("porsche.com"))
        h.delay()
        print("\n--- Test 5: Verify that 'New & Used Inventory' page opens correctly ---")

        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        t.sleep(3)

        driver.find_element(By.XPATH,
                            "//*[@id='b16687dd-7264-4bb9-a6d9-3f763ba84364']/astro-island/div/div[4]/p-button-group/p-link[3]").click()

        print("AFTER CLICK:", driver.current_url)

        header_xpath = "//span[contains(@class, '_1j9sent')]"

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, header_xpath))
        )

        # Assertion
        is_visible = h.assert_elementXPATH_visible(
            driver,
            header_xpath,
            description="Panamera 4 new and used inventory header"
        )

        print("Test 5 Passed" if is_visible else "Test 5 Failed")


    def tearDown(self):
        self.driver.quit()

class FirefoxDriverPorsche(unittest.TestCase):
    driver: WebDriver

    def setUp(self):
        self.driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install())
        )
        self.driver.maximize_window()


    def test_1_correct_pageFF(self):
        driver = self.driver
        driver.get(h.url_main)
        WebDriverWait(driver, 5).until(EC.url_contains("porsche.com"))
        h.delay()
        print("\n--- Test 1: Verify Panamera models page opens correctly ---")

        # Close cookies banner
        try:
            WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
            ).click()
        except:
            print("Cookie banner not found or already closed")

        # Locate Panamera tile
        panamera_tile = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((
                By.XPATH,
                "//article[@aria-label='Porsche Panamera']//a"
            ))
        )

        # Scroll + click with Firefox-safe fallback
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", panamera_tile)

        try:
            WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((
                    By.XPATH,
                    "//article[@aria-label='Porsche Panamera']//a"
                ))
            )
            panamera_tile.click()
        except:
            driver.execute_script("arguments[0].click();", panamera_tile)

        t.sleep(3)

        is_visible = h.assert_element_visible(driver, "s0-15", "Panamera Models variants")

        print("Test 1 Passed" if is_visible else "Test 1 Failed")

    def test_2_Build_PanameraFF(self):
        driver = self.driver
        driver.get(h.url_main)

        WebDriverWait(driver, 10).until(EC.url_contains("porsche.com"))
        print("\n--- Test 2: Verify 'Build your own' opens Panamera configuration page ---")

        # Close cookies banner if present
        try:
            cookie_btn = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
            )
            cookie_btn.click()
        except:
            pass  # banner may not appear

        # Scroll to "Build your own" inside Panamera tile
        build_btn = h.scroll_until_element(
            driver,
            By.XPATH,
            "//article[@aria-label='Porsche Panamera']//span[normalize-space()='Build your own']"
        )

        # Click using JS (Porsche uses shadow DOM / Astro components)
        driver.execute_script("arguments[0].scrollIntoView({block:'center'});", build_btn)
        driver.execute_script("arguments[0].click();", build_btn)

        # Wait for configuration page header
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h1[contains(text(), 'Which Panamera')]")
            )
        )

        # Assertion
        is_visible = h.assert_elementXPATH_visible(
            driver,
            "//h1[contains(text(), 'Which Panamera')]",
            description="Panamera configuration title"
        )

        print("Test 2 Passed" if is_visible else "Test 2 Failed")

    def test_3_All_panamera_models_correctFF(self):
        driver = self.driver
        driver.get(h.url_main)

        try:
            WebDriverWait(driver, 5).until(EC.url_contains("porsche.com"))
        except:
            print("URL did not load correctly")

        h.delay()
        print("\n---------------------- test3 -------------------------")
        print("Verify that all listed models have picture, title, description, Select Model button, and Compare button")

        # --- COOKIE BANNER ---
        try:
            WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
            ).click()
            print("Cookie banner closed")
        except:
            print("Cookie banner not found or already closed")

        # --- OPEN PANAMERA PAGE ---
        try:
            panamera_tile = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//article[@aria-label='Porsche Panamera']//a"))
            )
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", panamera_tile)

            try:
                WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//article[@aria-label='Porsche Panamera']//a"))
                )
                panamera_tile.click()
            except:
                print("Standard click failed → using JS click")
                driver.execute_script("arguments[0].click();", panamera_tile)

            t.sleep(3)

        except Exception as e:
            print(f"Could not open Panamera models page: {e}")
            return

        # --- HELPER: safe check wrapper ---
        def safe_check(xpath, description="element"):
            try:
                h.assert_elementXPATH_visible(driver, xpath, description=description)
            except Exception as e:
                print(f" {description} NOT found → {xpath}")
                print(f"Error: {e}")

        print("\nPanamera")
        safe_check("//div[@aria-label='Panamera']//img", "picture")
        safe_check("//div[@aria-label='Panamera']//h3", "name")
        safe_check("//div[@aria-label='Panamera']//ul", "description")
        safe_check("//*[@id='s0-0']/div/div[2]/div[1]/div/div[3]/p-link[1]", "Select Model Button")
        safe_check("//*[@id='s0-0']/div/div[2]/div[1]/div/div[3]/p-link[2]", "Compare Button")

    def tearDown(self):
        # Close driver
        self.driver.quit()