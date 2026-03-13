import sys
import os
import time
import unittest
import allure
import pytest
from selenium.webdriver.support.ui import WebDriverWait

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from helpers import (
    create_driver,
    deep_scan,
    slow_type,
    click_accept_all,
    click_burger,
    click_by_text,
    click_change_model,
    click_build_your_porsche,
    click_inventory,
    click_compare,
    find_zip_input,
    find_equipment_search_input,
    find_model_search_input,
    click_select_model,
    find_add_checkboxes,
    count_checked,
    click_checkbox_by_name,
    click_reset_filters,
    is_reset_button_enabled,
)

# ===========================================================================
# pytest fixture
# Читает браузер из переменной окружения BROWSER (default: chrome).
# Запуск всех тестов в 3 браузерах по очереди — через run_browsers.bat:
#   set BROWSER=chrome  && pytest ...
#   set BROWSER=firefox && pytest ...
#   set BROWSER=edge    && pytest ...
# ===========================================================================
@pytest.fixture
def browser():
    """
    Fixture читает BROWSER из env var.
    run_browsers.bat вызывает pytest 3 раза подряд,
    каждый раз с другим BROWSER=chrome/firefox/edge.
    """
    browser_name = os.environ.get("BROWSER", "chrome")
    allure.dynamic.parameter("browser", browser_name)
    driver = create_driver(browser_name)
    yield driver
    driver.quit()


# ===========================================================================
# Shared page-title constants
# ===========================================================================
TITLE_911_CARRERA  = "Porsche 911 Carrera | Porsche USA"
TITLE_CONFIGURATOR = "911 Carrera | Porsche Car Configurator (United States)"
TITLE_INVENTORY    = "Porsche 911 Carrera New and pre-owned cars for sale. | Porsche Finder"
TITLE_COMPARE      = "Compare Porsche 911 models | Porsche (United States)"


# ===========================================================================
# Shared navigation helpers
# ===========================================================================
def setup_homepage(driver):
    """Open porsche.com/usa and accept cookies."""
    driver.get("https://www.porsche.com/usa/")
    time.sleep(3)
    assert click_accept_all(driver), "Accept All button not found"


def open_carrera_drawer(driver):
    """Burger → 911 → 911 Carrera."""
    assert click_burger(driver), "Burger menu not found"
    assert click_by_text(driver, "911"), "'911' not found in menu"
    assert click_by_text(driver, "911 Carrera"), "'911 Carrera' not found in drawer"
    time.sleep(3)


def wait_for_title(driver, expected, timeout=20):
    """Poll driver.title until it matches or timeout."""
    deadline = time.time() + timeout
    while time.time() < deadline:
        if driver.title == expected:
            return True
        time.sleep(0.5)
    return False


def assert_title_and_url(driver, expected_title, expected_url_part):
    """Assert page <title> and URL fragment. Shows both expected and actual on failure."""
    title_ok = wait_for_title(driver, expected_title)
    assert title_ok, (
        f"\n  Expected title : '{expected_title}'"
        f"\n  Actual title   : '{driver.title}'"
        f"\n  Current URL    : {driver.current_url}"
    )
    assert expected_url_part in driver.current_url, (
        f"\n  Expected URL part : '{expected_url_part}'"
        f"\n  Actual URL        : {driver.current_url}"
    )


# ===========================================================================
#
#  POSITIVE TESTS  TC_P_001 … TC_P_005
#
#  Each function receives the `browser` fixture.
#  pytest will call them in this exact order for each browser:
#    test_TCP001 [chrome] → test_TCP002 [chrome] → … → test_NEG005 [chrome]
#    test_TCP001 [firefox] → …
#    test_TCP001 [edge]    → …
#
# ===========================================================================

@allure.feature("Porsche Navigation Flow")
@allure.story("TC_P_001 — Navigate to 911 Carrera page")
@allure.title("TC_P_001 — Burger → 911 → 911 Carrera | verify page title")
def test_TCP001_open_911_carrera(browser):
    driver = browser
    allure.dynamic.parameter("browser", driver.capabilities["browserName"])

    with allure.step("Open Porsche USA homepage and accept cookies"):
        setup_homepage(driver)

    with allure.step("Burger → 911 → 911 Carrera"):
        open_carrera_drawer(driver)

    with allure.step(f"Verify title = '{TITLE_911_CARRERA}' | URL contains porsche.com/usa"):
        assert_title_and_url(driver, TITLE_911_CARRERA, "porsche.com/usa")


@allure.feature("Porsche Navigation Flow")
@allure.story("TC_P_002 — Change model stays on 911 Carrera page")
@allure.title("TC_P_002 — Click 'Change model' | verify page title unchanged")
def test_TCP002_change_model(browser):
    driver = browser
    allure.dynamic.parameter("browser", driver.capabilities["browserName"])

    with allure.step("Open Porsche USA homepage and accept cookies"):
        setup_homepage(driver)

    with allure.step("Burger → 911 → 911 Carrera"):
        open_carrera_drawer(driver)

    with allure.step("Click 'Change model'"):
        assert click_change_model(driver), "'Change model' button not found"
        time.sleep(3)

    with allure.step(f"Verify title = '{TITLE_911_CARRERA}' | URL contains porsche.com/usa"):
        assert_title_and_url(driver, TITLE_911_CARRERA, "porsche.com/usa")


@allure.feature("Porsche Navigation Flow")
@allure.story("TC_P_003 — Build Your Porsche opens configurator")
@allure.title("TC_P_003 — Click 'Build Your Porsche' | verify configurator page title")
def test_TCP003_build_your_porsche(browser):
    driver = browser
    allure.dynamic.parameter("browser", driver.capabilities["browserName"])

    with allure.step("Open Porsche USA homepage and accept cookies"):
        setup_homepage(driver)

    with allure.step("Burger → 911 → 911 Carrera"):
        open_carrera_drawer(driver)

    with allure.step("Click 'Build Your Porsche'"):
        assert click_build_your_porsche(driver), "'Build Your Porsche' link not found"
        time.sleep(5)

    with allure.step(f"Verify title = '{TITLE_CONFIGURATOR}' | URL contains configurator.porsche.com"):
        assert_title_and_url(driver, TITLE_CONFIGURATOR, "configurator.porsche.com")


@allure.feature("Porsche Navigation Flow")
@allure.story("TC_P_004 — New and Used Inventory opens Porsche Finder")
@allure.title("TC_P_004 — Click 'New and Used Inventory' | verify Finder page title")
def test_TCP004_inventory(browser):
    driver = browser
    allure.dynamic.parameter("browser", driver.capabilities["browserName"])

    with allure.step("Open Porsche USA homepage and accept cookies"):
        setup_homepage(driver)

    with allure.step("Burger → 911 → 911 Carrera"):
        open_carrera_drawer(driver)

    with allure.step("Click 'New and Used Inventory'"):
        assert click_inventory(driver), "'New and Used Inventory' link not found"
        time.sleep(5)

    with allure.step(f"Verify title = '{TITLE_INVENTORY}' | URL contains finder.porsche.com"):
        assert_title_and_url(driver, TITLE_INVENTORY, "finder.porsche.com")


@allure.feature("Porsche Navigation Flow")
@allure.story("TC_P_005 — Compare opens compare page")
@allure.title("TC_P_005 — Click 'Compare' | verify compare page title")
def test_TCP005_compare(browser):
    driver = browser
    allure.dynamic.parameter("browser", driver.capabilities["browserName"])

    with allure.step("Open Porsche USA homepage and accept cookies"):
        setup_homepage(driver)

    with allure.step("Burger → 911"):
        assert click_burger(driver), "Burger menu not found"
        assert click_by_text(driver, "911"), "'911' not found"
        time.sleep(2)

    with allure.step("Click 'Compare'"):
        assert click_compare(driver), "'Compare' link not found"
        time.sleep(5)

    with allure.step(f"Verify title = '{TITLE_COMPARE}' | URL contains compare.porsche.com"):
        assert_title_and_url(driver, TITLE_COMPARE, "compare.porsche.com")


# ===========================================================================
#
#  NEGATIVE TESTS  NEG_001 … NEG_005
#
# ===========================================================================

@allure.feature("Porsche Negative Tests")
@allure.story("NEG_001 — Compare model limit")
@allure.title("NEG_001 — Cannot add more than 2 models to comparison")
def test_NEG001_compare_limit(browser):
    driver = browser
    allure.dynamic.parameter("browser", driver.capabilities["browserName"])

    with allure.step("Open compare page for 911"):
        driver.get("https://compare.porsche.com/en-US?model-series=911")
        WebDriverWait(driver, 10).until(lambda d: d.find_element("tag name", "body"))

    with allure.step("Accept cookies"):
        click_accept_all(driver)

    with allure.step("Select 1st model and check checkbox"):
        click_select_model(driver, 0)
        WebDriverWait(driver, 10).until(lambda d: len(find_add_checkboxes(d)) > 0)
        driver.execute_script("arguments[0].click()", find_add_checkboxes(driver)[0])

    with allure.step("Select 2nd model and check checkbox"):
        click_select_model(driver, 1)
        WebDriverWait(driver, 10).until(lambda d: len(find_add_checkboxes(d)) > 1)
        driver.execute_script("arguments[0].click()", find_add_checkboxes(driver)[1])

    with allure.step("Verify exactly 2 models checked"):
        assert count_checked(driver) == 2, "Expected 2 checked models"

    with allure.step("Try to add a 3rd model"):
        click_select_model(driver, 1)
        WebDriverWait(driver, 10).until(lambda d: len(find_add_checkboxes(d)) > 2)
        driver.execute_script("arguments[0].click()", find_add_checkboxes(driver)[2])

    with allure.step("Verify 'Maximum number reached' warning appears"):
        tooltip = False
        for el in deep_scan(driver):
            try:
                if "Maximum number reached" in driver.execute_script(
                        "return arguments[0].textContent.trim()", el):
                    tooltip = True
                    break
            except Exception:
                pass
        assert tooltip, "Expected 'Maximum number reached' tooltip — not found"

    with allure.step("Verify count still equals 2 (3rd not added)"):
        assert count_checked(driver) == 2, "Count should stay at 2"


@allure.feature("Porsche Negative Tests")
@allure.story("NEG_002 — Equipment search: special chars return 0 results")
@allure.title("NEG_002 — Configurator search: @#$%/- symbols return 0 results, page stable")
def test_NEG002_equipment_search_special_chars(browser):
    driver = browser
    allure.dynamic.parameter("browser", driver.capabilities["browserName"])

    with allure.step("Open Porsche USA and navigate to configurator"):
        setup_homepage(driver)
        open_carrera_drawer(driver)
        assert click_build_your_porsche(driver), "'Build Your Porsche' not found"
        time.sleep(6)

    with allure.step("Find equipment search input"):
        search_input = find_equipment_search_input(driver)
        assert search_input is not None, "Equipment search input not found"

    with allure.step("Enter valid text 'Sport' — must be accepted"):
        search_input.clear()
        slow_type(search_input, "Sport")
        time.sleep(1)
        assert search_input.get_attribute("value") == "Sport", "Valid text 'Sport' was not accepted"

    with allure.step("Clear and enter special characters '@#$%/-'"):
        search_input.clear()
        slow_type(search_input, "@#$%/-")
        time.sleep(2)

    with allure.step("Verify page stays stable after special chars input"):
        assert driver.execute_script("return document.readyState") == "complete"

    with allure.step("Verify 0 equipment results for special chars"):
        count = sum(
            1 for el in deep_scan(driver)
            if _safe_tag(el) in ("icc-option", "icc-search-result-item")
            and _safe_displayed(el)
        )
        assert count == 0, f"Expected 0 results for '@#$%/-', got {count}"


@allure.feature("Porsche Negative Tests")
@allure.story("NEG_003 — Dealer ZIP input validation")
@allure.title("NEG_003 — ZIP field: digits accepted, special chars return 0 dealer cards")
def test_NEG003_zip_input_validation(browser):
    driver = browser
    allure.dynamic.parameter("browser", driver.capabilities["browserName"])

    with allure.step("Navigate to dealer search page"):
        _navigate_to_dealer_search(driver)

    with allure.step("Find ZIP / City input"):
        zip_input = find_zip_input(driver)
        assert zip_input is not None, "ZIP/City input not found"

    with allure.step("Enter valid ZIP '90210' — must be accepted"):
        zip_input.clear()
        time.sleep(0.5)
        zip_input.send_keys("90210")
        time.sleep(1)
        val = zip_input.get_attribute("value")
        assert "90210" in val, f"Valid ZIP digits should be accepted, got: '{val}'"

    with allure.step("Clear field"):
        zip_input.clear()
        time.sleep(0.5)

    with allure.step("Enter special chars '@#$%' — 0 dealer cards expected"):
        zip_input.send_keys("@#$%")
        time.sleep(2)
        result_count = sum(
            1 for el in deep_scan(driver)
            if _safe_tag(el) in ("phn-dealer-result-item", "phn-dealer-card")
            and _safe_displayed(el)
        )
        assert result_count == 0, \
            f"Special chars should return 0 dealer cards, got {result_count}"

    with allure.step("Verify page is stable"):
        assert driver.execute_script("return document.readyState") == "complete"


@allure.feature("Porsche Negative Tests")
@allure.story("NEG_004 — Models search with invalid input stays stable")
@allure.title("NEG_004 — Invalid symbols in model search do not break the page")
def test_NEG004_model_search_invalid_input(browser):
    driver = browser
    allure.dynamic.parameter("browser", driver.capabilities["browserName"])
    invalid_text = "@@@###$$$%%%^^^&&&***"

    with allure.step("Open 911 models page"):
        driver.get("https://models.porsche.com/en-US/model-start/911")
        time.sleep(4)

    with allure.step("Accept cookies"):
        click_accept_all(driver)

    with allure.step("Find model search input"):
        search_input = find_model_search_input(driver)
        assert search_input is not None, "Model search input not found"

    with allure.step(f"Inject invalid text via JS: '{invalid_text}'"):
        driver.execute_script("arguments[0].value = arguments[1]", search_input, invalid_text)
        driver.execute_script("""
            arguments[0].dispatchEvent(new Event('input',  { bubbles: true }));
            arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
        """, search_input)
        time.sleep(2)

    with allure.step("Verify page is still stable (readyState = complete)"):
        assert driver.execute_script("return document.readyState") == "complete"

    with allure.step("Verify body element is accessible"):
        assert driver.find_element("tag name", "body") is not None


@allure.feature("Porsche Negative Tests")
@allure.story("NEG_005 — Reset All Filters unchecks all applied filters")
@allure.title("NEG_005 — After Reset All Filters all checkboxes are unchecked")
def test_NEG005_reset_filters(browser):
    driver = browser
    allure.dynamic.parameter("browser", driver.capabilities["browserName"])

    with allure.step("Open 911 models page"):
        driver.get("https://models.porsche.com/en-US/model-start/911")
        time.sleep(4)

    with allure.step("Accept cookies"):
        click_accept_all(driver)

    with allure.step("Apply multiple filters"):
        applied = []
        for name in ["Carrera", "Carrera Cabriolet", "Targa", "Automatic", "GT"]:
            if click_checkbox_by_name(driver, name):
                applied.append(name)
        for el in deep_scan(driver):
            try:
                if el.get_attribute("id") == "checkbox_all_wheel_drive":
                    driver.execute_script("arguments[0].click()", el)
                    applied.append("All Wheel Drive")
                    break
            except Exception:
                pass
        time.sleep(2)
        assert len(applied) > 0, "No filters were applied"

    with allure.step("Verify at least one checkbox is checked before reset"):
        before = _get_checked_unique(driver)
        assert len(before) > 0, "No checked checkboxes found before reset"

    with allure.step("Verify 'Reset All Filters' button is enabled before click"):
        assert is_reset_button_enabled(driver), "'Reset All Filters' button is disabled"

    with allure.step("Click 'Reset All Filters' and wait for DOM to settle"):
        assert click_reset_filters(driver), "Reset All Filters button not found"
        deadline = time.time() + 8
        after = _get_checked_unique(driver)
        while after and time.time() < deadline:
            time.sleep(0.5)
            after = _get_checked_unique(driver)

    with allure.step("Verify all checkboxes are unchecked after reset"):
        assert len(after) == 0, f"Expected 0 checked after reset, still: {after}"

    with allure.step("Verify UI is stable"):
        assert driver.execute_script("return document.readyState") == "complete"


# ===========================================================================
# Private helper functions
# ===========================================================================

def _navigate_to_dealer_search(driver):
    driver.get("https://www.porsche.com/usa/")
    time.sleep(4)
    click_accept_all(driver)
    click_burger(driver)
    time.sleep(1)

    found = False
    for el in deep_scan(driver):
        try:
            if el.get_attribute("data-id") == "find_a_dealer":
                driver.execute_script("arguments[0].scrollIntoView({block:'center'})", el)
                driver.execute_script("arguments[0].click()", el)
                found = True
                break
        except Exception:
            pass

    if not found:
        for phrase in ("Find Your Porsche Center", "Find a Dealer", "Porsche Center"):
            for el in deep_scan(driver):
                try:
                    txt = driver.execute_script("return arguments[0].textContent.trim()", el)
                    if phrase in txt and el.tag_name.lower() in ("button", "a", "span", "p"):
                        driver.execute_script("arguments[0].scrollIntoView({block:'center'})", el)
                        driver.execute_script("arguments[0].click()", el)
                        found = True
                        break
                except Exception:
                    pass
            if found:
                break

    if not found:
        driver.get("https://finder.porsche.com/usa/en-US/dealer")
        time.sleep(3)
        return

    time.sleep(2)
    for el in deep_scan(driver):
        try:
            if el.tag_name.lower() == "a":
                txt = driver.execute_script("return arguments[0].textContent.trim()", el)
                if "dealers on a map" in txt or "Search for dealers" in txt:
                    driver.execute_script("arguments[0].click()", el)
                    break
        except Exception:
            pass
    time.sleep(2)


def _get_checked_unique(driver):
    seen, result = set(), []
    for el in deep_scan(driver):
        try:
            if el.tag_name.lower() == "input" and el.get_attribute("type") == "checkbox":
                if el.is_selected():
                    name = el.get_attribute("name") or el.get_attribute("id") or "?"
                    if name not in seen:
                        seen.add(name)
                        result.append(name)
        except Exception:
            pass
    return result


def _safe_tag(el):
    try:
        return el.tag_name.lower()
    except Exception:
        return ""


def _safe_displayed(el):
    try:
        return el.is_displayed()
    except Exception:
        return False


# ===========================================================================
# unittest entry point — PyCharm green-play button
# Single browser, controlled by BROWSER env var (default: chrome)
# ===========================================================================
class BasePorscheTest(unittest.TestCase):
    _browser = os.environ.get("BROWSER", "chrome")

    def setUp(self):
        self.driver = create_driver(self._browser)

    def tearDown(self):
        self.driver.quit()


@pytest.mark.skip(reason="Дубликат pytest-тестов, используем только pytest-версию")
class TestPorscheUnittest(BasePorscheTest):

    def test_TCP001_open_911_carrera(self):
        setup_homepage(self.driver)
        open_carrera_drawer(self.driver)
        assert_title_and_url(self.driver, TITLE_911_CARRERA, "porsche.com/usa")

    def test_TCP002_change_model(self):
        setup_homepage(self.driver)
        open_carrera_drawer(self.driver)
        assert click_change_model(self.driver), "'Change model' not found"
        time.sleep(3)
        assert_title_and_url(self.driver, TITLE_911_CARRERA, "porsche.com/usa")

    def test_TCP003_build_your_porsche(self):
        setup_homepage(self.driver)
        open_carrera_drawer(self.driver)
        assert click_build_your_porsche(self.driver), "'Build Your Porsche' not found"
        time.sleep(5)
        assert_title_and_url(self.driver, TITLE_CONFIGURATOR, "configurator.porsche.com")

    def test_TCP004_inventory(self):
        setup_homepage(self.driver)
        open_carrera_drawer(self.driver)
        assert click_inventory(self.driver), "'Inventory' not found"
        time.sleep(5)
        assert_title_and_url(self.driver, TITLE_INVENTORY, "finder.porsche.com")

    def test_TCP005_compare(self):
        setup_homepage(self.driver)
        assert click_burger(self.driver)
        assert click_by_text(self.driver, "911")
        time.sleep(2)
        assert click_compare(self.driver)
        time.sleep(5)
        assert_title_and_url(self.driver, TITLE_COMPARE, "compare.porsche.com")

    def test_NEG001_compare_limit(self):
        d = self.driver
        d.get("https://compare.porsche.com/en-US?model-series=911")
        WebDriverWait(d, 10).until(lambda x: x.find_element("tag name", "body"))
        click_accept_all(d)
        click_select_model(d, 0)
        WebDriverWait(d, 10).until(lambda x: len(find_add_checkboxes(x)) > 0)
        d.execute_script("arguments[0].click()", find_add_checkboxes(d)[0])
        click_select_model(d, 1)
        WebDriverWait(d, 10).until(lambda x: len(find_add_checkboxes(x)) > 1)
        d.execute_script("arguments[0].click()", find_add_checkboxes(d)[1])
        self.assertEqual(count_checked(d), 2)
        click_select_model(d, 1)
        WebDriverWait(d, 10).until(lambda x: len(find_add_checkboxes(x)) > 2)
        d.execute_script("arguments[0].click()", find_add_checkboxes(d)[2])
        tooltip = any(
            "Maximum number reached" in (d.execute_script(
                "return arguments[0].textContent.trim()", el) or "")
            for el in deep_scan(d)
        )
        self.assertTrue(tooltip)
        self.assertEqual(count_checked(d), 2)

    def test_NEG002_equipment_search_special_chars(self):
        d = self.driver
        setup_homepage(d)
        open_carrera_drawer(d)
        assert click_build_your_porsche(d)
        time.sleep(6)
        inp = find_equipment_search_input(d)
        self.assertIsNotNone(inp)
        inp.clear()
        slow_type(inp, "Sport")
        time.sleep(1)
        self.assertEqual(inp.get_attribute("value"), "Sport")
        inp.clear()
        slow_type(inp, "@#$%/-")
        time.sleep(2)
        self.assertEqual(d.execute_script("return document.readyState"), "complete")
        count = sum(1 for el in deep_scan(d)
                    if _safe_tag(el) in ("icc-option", "icc-search-result-item")
                    and _safe_displayed(el))
        self.assertEqual(count, 0)

    def test_NEG003_zip_input_validation(self):
        d = self.driver
        _navigate_to_dealer_search(d)
        zi = find_zip_input(d)
        self.assertIsNotNone(zi)
        zi.clear()
        time.sleep(0.5)
        zi.send_keys("90210")
        time.sleep(1)
        self.assertIn("90210", zi.get_attribute("value"))
        zi.clear()
        time.sleep(0.5)
        zi.send_keys("@#$%")
        time.sleep(2)
        rc = sum(1 for el in deep_scan(d)
                 if _safe_tag(el) in ("phn-dealer-result-item", "phn-dealer-card")
                 and _safe_displayed(el))
        self.assertEqual(rc, 0)
        self.assertEqual(d.execute_script("return document.readyState"), "complete")

    def test_NEG004_model_search_invalid_input(self):
        d = self.driver
        d.get("https://models.porsche.com/en-US/model-start/911")
        time.sleep(4)
        click_accept_all(d)
        inp = find_model_search_input(d)
        self.assertIsNotNone(inp)
        d.execute_script("arguments[0].value = arguments[1]", inp, "@@@###$$$")
        d.execute_script("""
            arguments[0].dispatchEvent(new Event('input',  { bubbles: true }));
            arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
        """, inp)
        time.sleep(2)
        self.assertEqual(d.execute_script("return document.readyState"), "complete")
        self.assertIsNotNone(d.find_element("tag name", "body"))

    def test_NEG005_reset_filters(self):
        d = self.driver
        d.get("https://models.porsche.com/en-US/model-start/911")
        time.sleep(4)
        click_accept_all(d)
        applied = [n for n in ["Carrera", "Carrera Cabriolet", "Targa", "Automatic", "GT"]
                   if click_checkbox_by_name(d, n)]
        for el in deep_scan(d):
            try:
                if el.get_attribute("id") == "checkbox_all_wheel_drive":
                    d.execute_script("arguments[0].click()", el)
                    break
            except Exception:
                pass
        time.sleep(2)
        self.assertGreater(len(applied), 0)
        self.assertGreater(len(_get_checked_unique(d)), 0)
        self.assertTrue(is_reset_button_enabled(d))
        self.assertTrue(click_reset_filters(d))
        deadline = time.time() + 8
        after = _get_checked_unique(d)
        while after and time.time() < deadline:
            time.sleep(0.5)
            after = _get_checked_unique(d)
        self.assertEqual(len(after), 0, f"Still checked: {after}")
        self.assertEqual(d.execute_script("return document.readyState"), "complete")


if __name__ == "__main__":
    unittest.main(verbosity=2)
