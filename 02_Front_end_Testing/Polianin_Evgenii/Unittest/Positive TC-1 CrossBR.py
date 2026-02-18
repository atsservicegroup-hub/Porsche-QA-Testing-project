from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
import time


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


def run_test(browser_name):
    print(f"\n==============================")
    print(f"STARTING TEST IN: {browser_name}")
    print(f"==============================")

    # --- 1. Browser initialization ---
    if browser_name == "chrome":
        driver = webdriver.Chrome()

    elif browser_name == "edge":
        driver = webdriver.Edge(service=EdgeService())

    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=FirefoxService())

    else:
        raise ValueError("Unknown browser")

    driver.maximize_window()
    driver.get("https://www.porsche.com/usa/")
    time.sleep(4)

    # --- 2. Accept All ---
    elements = deep_scan(driver)
    for el in elements:
        try:
            if driver.execute_script("return arguments[0].textContent.trim()", el) == "Accept All":
                driver.execute_script("arguments[0].click()", el)
                print("✔ Accept All clicked")
                break
        except:
            pass

    time.sleep(2)

    # --- 3. Burger menu ---
    elements = deep_scan(driver)
    burger = None
    for el in elements:
        try:
            aria = el.get_attribute("aria-label") or ""
            if "menu" in aria.lower():
                burger = el
                break
        except:
            pass

    driver.execute_script("arguments[0].click()", burger)
    print("✔ Burger menu opened")
    time.sleep(1)

    # --- 4. Click “911” ---
    elements = deep_scan(driver)
    for el in elements:
        try:
            if driver.execute_script("return arguments[0].textContent.trim()", el) == "911":
                driver.execute_script("arguments[0].click()", el)
                print("✔ 911 clicked")
                break
        except:
            pass

    time.sleep(1)

    # --- 5. Click “911 Carrera” in header ---
    elements = deep_scan(driver)
    carrera_el = None

    for el in elements:
        try:
            txt = driver.execute_script("return arguments[0].textContent.trim()", el)
            if txt == "911 Carrera":
                carrera_el = el
                break
        except:
            pass

    if not carrera_el:
        print(" 911 Carrera element not found in header")
        driver.quit()
        return

    driver.execute_script("arguments[0].click()", carrera_el)
    print("✔ Clicked 911 Carrera")

    time.sleep(5)

    print(f"🌐 URL in {browser_name}: {driver.current_url}")

    driver.quit()
    print(f"✔ TEST FINISHED IN: {browser_name}")


# ============================
# Running tests in 3 browsers
# ============================

for browser in ["chrome", "edge", "firefox"]:
    run_test(browser)
