import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.options import Options as Edge_Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


# ===========================================================================
# create_driver — supports chrome / firefox / edge
#
# Usage:
#   driver = create_driver()            # uses BROWSER env var, default: chrome
#   driver = create_driver("firefox")   # explicit browser name
#
# Windows env var:  set BROWSER=firefox
# Mac/Linux:        export BROWSER=firefox
# ===========================================================================

def create_driver(browser: str = None) -> webdriver.Remote:
    browser = (browser or os.environ.get("BROWSER", "chrome")).lower().strip()

    if browser == "firefox":
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options,
        )

    elif browser == "edge":
        # SE_DRIVER_MIRROR_URL tells webdriver-manager to fetch
        # msedgedriver from the official Microsoft CDN.
        os.environ["SE_DRIVER_MIRROR_URL"] = "https://msedgedriver.microsoft.com"
        options = Edge_Options()
        options.add_argument("--disable-blink-features=AutomationControlled")
        driver = webdriver.Edge(options=options)

    else:  # chrome (default)
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")

        # Prefer already-downloaded chromedriver from local cache to avoid
        # сетевые ошибки к googlechromelabs при каждом запуске.
        cached_driver = os.path.expanduser(
            r"~\.wdm\drivers\chromedriver\win64\145.0.7632.117\chromedriver-win32\chromedriver.exe"
        )
        if os.path.exists(cached_driver):
            service = ChromeService(cached_driver)
        else:
            service = ChromeService(ChromeDriverManager().install())

        driver = webdriver.Chrome(
            service=service,
            options=options,
        )

    driver.maximize_window()
    return driver


# ===========================================================================
# Deep scan — traverses regular DOM + shadow DOM recursively
# ===========================================================================
def deep_scan(driver):
    return driver.execute_script("""
        function deep(node, acc) {
            if (!node) return;
            acc.push(node);
            if (node.children) {
                for (let c of node.children) deep(c, acc);
            }
            if (node.shadowRoot) {
                deep(node.shadowRoot, acc);
            }
        }
        let all = [];
        deep(document.body, all);
        return all;
    """)


# ===========================================================================
# Generic helpers
# ===========================================================================
def slow_type(element, text, delay=0.2):
    for ch in text:
        element.send_keys(ch)
        time.sleep(delay)


def wait_for_text(driver, text, timeout=10):
    end = time.time() + timeout
    while time.time() < end:
        for el in deep_scan(driver):
            try:
                if driver.execute_script("return arguments[0].textContent.trim()", el) == text:
                    return el
            except Exception:
                pass
        time.sleep(0.2)
    return None


def click_by_text(driver, text):
    el = wait_for_text(driver, text, timeout=10)
    if el:
        driver.execute_script("arguments[0].scrollIntoView({block:'center'})", el)
        driver.execute_script("arguments[0].click()", el)
        return True
    return False


def click_accept_all(driver):
    time.sleep(1)
    return click_by_text(driver, "Accept All")


def click_burger(driver):
    end = time.time() + 10
    while time.time() < end:
        for el in deep_scan(driver):
            try:
                aria = el.get_attribute("aria-label") or ""
                if "menu" in aria.lower():
                    driver.execute_script("arguments[0].click()", el)
                    return True
            except Exception:
                pass
        time.sleep(0.2)
    return False


def click_change_model(driver):
    return click_by_text(driver, "Change model")


def click_build_your_porsche(driver):
    end = time.time() + 10
    while time.time() < end:
        for el in deep_scan(driver):
            try:
                if el.tag_name.lower() == "a":
                    href = el.get_attribute("href") or ""
                    if "configurator.porsche.com" in href:
                        driver.execute_script("arguments[0].scrollIntoView({block:'center'})", el)
                        driver.execute_script("arguments[0].click()", el)
                        return True
            except Exception:
                pass
        time.sleep(0.2)
    return False


def click_inventory(driver):
    end = time.time() + 10
    while time.time() < end:
        for el in deep_scan(driver):
            try:
                if el.tag_name.lower() == "a":
                    href = el.get_attribute("href") or ""
                    if "finder.porsche.com" in href:
                        driver.execute_script("arguments[0].scrollIntoView({block:'center'})", el)
                        driver.execute_script("arguments[0].click()", el)
                        return True
            except Exception:
                pass
        time.sleep(0.2)
    return False


def click_compare(driver):
    end = time.time() + 10
    while time.time() < end:
        for el in deep_scan(driver):
            try:
                if el.tag_name.lower() == "a":
                    href = el.get_attribute("href") or ""
                    if "compare.porsche.com" in href:
                        driver.execute_script("arguments[0].scrollIntoView({block:'center'})", el)
                        driver.execute_script("arguments[0].click()", el)
                        return True
            except Exception:
                pass
        time.sleep(0.2)
    return False


def find_zip_input(driver, timeout=10):
    end = time.time() + timeout
    while time.time() < end:
        for el in deep_scan(driver):
            try:
                if el.tag_name.lower() == "input":
                    ph = el.get_attribute("placeholder") or ""
                    if "ZIP" in ph or "City" in ph:
                        return el
            except Exception:
                pass
        time.sleep(0.3)
    return None


def find_equipment_search_input(driver, timeout=10):
    end = time.time() + timeout
    while time.time() < end:
        for el in deep_scan(driver):
            try:
                if el.tag_name.lower() == "icc-p-input-search":
                    shadow = el.shadow_root
                    inp = shadow.find_element(By.CSS_SELECTOR, "input#input-search")
                    return inp
            except Exception:
                pass
        time.sleep(0.3)
    return None


def find_model_search_input(driver, timeout=10):
    end = time.time() + timeout
    while time.time() < end:
        for el in deep_scan(driver):
            try:
                if el.tag_name.lower() == "p-input-search":
                    shadow = el.shadow_root
                    inp = shadow.find_element(By.CSS_SELECTOR, "input#input-search")
                    return inp
            except Exception:
                pass
        time.sleep(0.3)
    return None


# ===========================================================================
# Compare-page helpers
# ===========================================================================
def click_select_model(driver, index=0):
    buttons = []
    for el in deep_scan(driver):
        try:
            if el.tag_name.lower() == "p-button":
                txt = driver.execute_script("return arguments[0].textContent.trim()", el)
                if txt == "Select model":
                    buttons.append(el)
        except Exception:
            pass
    shadow = buttons[index].shadow_root
    real_btn = shadow.find_element(By.CSS_SELECTOR, "button.root")
    driver.execute_script("arguments[0].click()", real_btn)


def find_add_checkboxes(driver):
    boxes = []
    for el in deep_scan(driver):
        try:
            if el.tag_name.lower() == "input" and el.get_attribute("type") == "checkbox":
                name = el.get_attribute("name") or ""
                if "Add" in name and "to comparison" in name:
                    boxes.append(el)
        except Exception:
            pass
    return boxes


def count_checked(driver):
    return sum(1 for el in find_add_checkboxes(driver) if el.is_selected())


# ===========================================================================
# Models-page filter helpers
# ===========================================================================
def click_checkbox_by_name(driver, name):
    for el in deep_scan(driver):
        try:
            if el.tag_name.lower() == "input" and el.get_attribute("type") == "checkbox":
                if el.get_attribute("name") == name:
                    driver.execute_script("arguments[0].click()", el)
                    return el
        except Exception:
            pass
    return None


def click_reset_filters(driver):
    for el in deep_scan(driver):
        try:
            if el.tag_name.lower() == "p-button":
                shadow = el.shadow_root
                btn = shadow.find_element(By.CSS_SELECTOR, "button.root")
                if btn.text.strip() == "Reset All Filters":
                    if not btn.is_enabled():
                        return False
                    # Click reset button
                    driver.execute_script("arguments[0].click()", btn)
                    # Extra safety: forcibly uncheck all checkboxes in DOM
                    driver.execute_script("""
                        document
                          .querySelectorAll('input[type="checkbox"]')
                          .forEach(cb => {
                              cb.checked = false;
                              cb.dispatchEvent(new Event('change', { bubbles: true }));
                          });
                    """)
                    return True
        except Exception:
            pass
    return False


def is_reset_button_enabled(driver):
    for el in deep_scan(driver):
        try:
            if el.tag_name.lower() == "p-button":
                shadow = el.shadow_root
                btn = shadow.find_element(By.CSS_SELECTOR, "button.root")
                if btn.text.strip() == "Reset All Filters":
                    return btn.is_enabled()
        except Exception:
            pass
    return False
