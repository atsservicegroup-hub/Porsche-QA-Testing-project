from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException
import time

url_main = "https://www.porsche.com/usa/"
url_panamera_models="https://www.porsche.com/usa/models/panamera/"

def delay(seconds=1):
    time.sleep(seconds)

def take_screenshot(driver, filename="screenshot.png"):
    driver.save_screenshot(filename)

    try:
        assert driver.find_element(By.XPATH, "//a[normalize-space()='Company']").is_displayed()
        assert driver.find_element(By.XPATH, "//a[normalize-space()='Company']").is_enabled()
        print("Company is displayed and enabled")
    except AssertionError:
        print("Company tab is not found")

def scroll_until_element(driver, by, locator, max_scrolls=30, pause=0.4):
    for _ in range(max_scrolls):
        try:
            element = driver.find_element(by, locator)
            driver.execute_script("arguments[0].scrollIntoView(true);", element)
            return element
        except NoSuchElementException:
            driver.execute_script("window.scrollBy(0, 800);")
            time.sleep(pause)

    raise Exception(f"element '{locator}' is not found  {max_scrolls} after scrolling")

def close_cookies(driver):
    try:
        btn = driver.find_element(By.CSS_SELECTOR, "button[mode='primary'], button[aria-label='Agree'], button")
        driver.execute_script("arguments[0].click();", btn)
    except NoSuchElementException:
        pass

def assert_element_visible(driver, elementid, description="element"):
  # Checks that element is displayed
    try:
        element = driver.find_element(By.ID, elementid)
        assert element.is_displayed()
        print(f"{description} is displayed")
        return True
    except NoSuchElementException:
        print(f"{description} is not displayed")
        take_screenshot(driver)
        return False
    except AssertionError:
        print(f"Something is wrong with {description}")
        take_screenshot(driver)
        return False


def assert_elementXPATH_visible(driver, elementxpath, description="element"):
    # Checks that element is displayed
    try:
        element = driver.find_element(By.XPATH, elementxpath)
        assert element.is_displayed()
        print(f"{description} is displayed")
        return True
    except NoSuchElementException:
        print(f"{description} is not displayed")
        take_screenshot(driver)
        return False
    except AssertionError:
        print(f"Something is wrong with {description}")
        take_screenshot(driver)
        return False






