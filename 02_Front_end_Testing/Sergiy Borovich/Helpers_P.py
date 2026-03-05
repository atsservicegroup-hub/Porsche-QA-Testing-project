from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
import requests
def delay():
    time.sleep(random.randint(1, 3))


def shopping_tools_button(driver):
    host = driver.find_element(By.CSS_SELECTOR, "phn-header")
    shadow = host.shadow_root
    shopping_tools = shadow.find_element(By.CSS_SELECTOR,"phn-p-button-pure[class='sc-phn-nd-side-drawer-item hydrated'][data-id='vehicle_purchase']")
    driver.execute_script("arguments[0].click();", shopping_tools)

def finding_menu_button(driver):
    host = driver.find_element(By.CSS_SELECTOR, "phn-header")
    shadow = host.shadow_root
    models = shadow.find_element(By.CSS_SELECTOR, "phn-p-button-pure")
    driver.execute_script("arguments[0].click();", models)

def build_your_own_button(driver):
    host = driver.find_element(By.CSS_SELECTOR, "phn-header")
    shadow = host.shadow_root
    build_your_own = shadow.find_element(By.CSS_SELECTOR,"a[class='pure-link sc-phn-nd-menu-item'][data-id='vehicle_purchase/mainmenu.vehiclepurchase.configure']")
    driver.execute_script("arguments[0].click();", build_your_own)

def compare_models_button(driver):
    host = driver.find_element(By.CSS_SELECTOR, "phn-header")
    shadow = host.shadow_root
    compare_models = shadow.find_element(By.CSS_SELECTOR,"a[class='pure-link sc-phn-nd-menu-item'][data-id='vehicle_purchase/mainmenu.vehiclepurchase.compare']")
    driver.execute_script("arguments[0].click();", compare_models)

def new_and_used_button(driver):
    host = driver.find_element(By.CSS_SELECTOR, "phn-header")
    shadow = host.shadow_root
    new_and_used = shadow.find_element(By.CSS_SELECTOR,"a[class='pure-link sc-phn-nd-menu-item'][data-id='vehicle_purchase/mainmenu.vehiclepurchase.findvehicles']")
    driver.execute_script("arguments[0].click();", new_and_used)

def current_vehicle_offers_button(driver):
    host = driver.find_element(By.CSS_SELECTOR, "phn-header")
    shadow = host.shadow_root
    current_vehicle_offers = shadow.find_element(By.CSS_SELECTOR,"a[class='pure-link sc-phn-nd-menu-item'][data-id='vehicle_purchase/mainmenu.vehiclepurchase.currentcaroffers']")
    driver.execute_script("arguments[0].click();", current_vehicle_offers)

def certified_button(driver):
    host = driver.find_element(By.CSS_SELECTOR, "phn-header")
    shadow = host.shadow_root
    certified = shadow.find_element(By.CSS_SELECTOR,"a[class='pure-link sc-phn-nd-menu-item'][data-id='vehicle_purchase/mainmenu.vehiclepurchase.approved']")
    driver.execute_script("arguments[0].click();", certified)

def porsche_financial_button(driver):
    host = driver.find_element(By.CSS_SELECTOR, "phn-header")
    shadow = host.shadow_root
    porsche_financial = shadow.find_element(By.CSS_SELECTOR,"a[class='pure-link sc-phn-nd-menu-item'][data-id='vehicle_purchase/mainmenu.vehiclepurchase.financialservices']")
    driver.execute_script("arguments[0].click();", porsche_financial)

def e_mobility_button(driver):
    host = driver.find_element(By.CSS_SELECTOR, "phn-header")
    shadow = host.shadow_root
    e_mobility = shadow.find_element(By.CSS_SELECTOR,"a[class='pure-link sc-phn-nd-menu-item'][data-id='vehicle_purchase/mainmenu.vehiclepurchase.eperformance']")
    driver.execute_script("arguments[0].click();", e_mobility)

def account_button(driver):
    host = driver.find_element(By.CSS_SELECTOR, "phn-header")
    shadow = host.shadow_root
    account = shadow.find_element(By.CSS_SELECTOR,"phn-p-button-pure[class='sc-phn-nd-side-drawer-item hydrated'][data-id='account']")
    driver.execute_script("arguments[0].click();", account)

def log_in_button(driver):
    host = driver.find_element(By.CSS_SELECTOR, "phn-header")
    shadow = host.shadow_root
    log_in = shadow.find_element(By.CSS_SELECTOR, ".login.sc-phn-nd-pcom-login.hydrated")
    driver.execute_script("arguments[0].click();", log_in)

def saved_searches_button(driver):
    host = driver.find_element(By.CSS_SELECTOR, "phn-header")
    shadow = host.shadow_root
    saved_searches = shadow.find_element(By.CSS_SELECTOR,"a[class='pure-link sc-phn-nd-menu-item'][data-id='account/mainmenu.account.savedsearches']")
    driver.execute_script("arguments[0].click();", saved_searches)

def saved_cars_button(driver):
    host = driver.find_element(By.CSS_SELECTOR, "phn-header")
    shadow = host.shadow_root
    saved_cars = shadow.find_element(By.CSS_SELECTOR,"a[class='pure-link sc-phn-nd-menu-item'][data-id='account/mainmenu.account.savedvehicles']")
    driver.execute_script("arguments[0].click();", saved_cars)

def find_connect_services_button(driver):
    host = driver.find_element(By.CSS_SELECTOR, "phn-header")
    shadow = host.shadow_root
    find_connect_services = shadow.find_element(By.CSS_SELECTOR,"a[class='pure-link sc-phn-nd-menu-item'][data-id='account/mainmenu.account.connect']")
    driver.execute_script("arguments[0].click();", find_connect_services)

def contact_and_support_button(driver):
    host = driver.find_element(By.CSS_SELECTOR, "phn-header")
    shadow = host.shadow_root
    contact_and_support = shadow.find_element(By.CSS_SELECTOR,"a[class='pure-link sc-phn-nd-menu-item'][data-id='account/mainmenu.account.contact']")
    driver.execute_script("arguments[0].click();", contact_and_support)



def check_porsche_url(driver):
    try:
        assert "https://www.porsche.com/usa/" in driver.current_url
        print("Test result: Page URL is: ", driver.current_url)
    except AssertionError:
        print("Test result: Page URL is different", driver.current_url)

def check_build_your_own_url(driver):
    try:
        assert "https://models.porsche.com/en-US/model-start" in driver.current_url
        print("Test result: Page URL is: ", driver.current_url)
    except AssertionError:
        print("Test result: Page URL is different", driver.current_url)

def check_compare_models_url(driver):
    try:
        assert "https://compare.porsche.com/en-US" in driver.current_url
        print("Test result: Page URL is: ", driver.current_url)
    except AssertionError:
        print("Test result: Page URL is different", driver.current_url)

def check_new_and_used_url(driver):
    try:
        assert "https://finder.porsche.com/us/en-US?int_ref=globalnav&int_medium=link&int_id=inventory" in driver.current_url
        print("Test result: Page URL is: ", driver.current_url)
    except AssertionError:
        print("Test result: Page URL is different", driver.current_url)

def check_current_vehicle_offers_url(driver):
    try:
        assert "https://www.porsche.com/usa/accessoriesandservice/porschefinancialservices/pfs-leasing-offers/" in driver.current_url
        print("Test result: Page URL is: ", driver.current_url)
    except AssertionError:
        print("Test result: Page URL is different", driver.current_url)

def check_certified_url(driver):
    try:
        assert "https://www.porsche.com/usa/approved-used/?int_ref=globalnav&int_medium=link&int_id=inventory" in driver.current_url
        print("Test result: Page URL is: ", driver.current_url)
    except AssertionError:
        print("Test result: Page URL is different", driver.current_url)

def check_porsche_financial_url(driver):
    try:
        assert "https://www.porsche.com/usa/accessoriesandservice/porschefinancialservices/" in driver.current_url
        print("Test result: Page URL is: ", driver.current_url)
    except AssertionError:
        print("Test result: Page URL is different", driver.current_url)

def check_e_mobility_url(driver):
    try:
        assert "https://www.porsche.com/usa/aboutporsche/e-performance/" in driver.current_url
        print("Test result: Page URL is: ", driver.current_url)
    except AssertionError:
        print("Test result: Page URL is different", driver.current_url)

def check_log_in_url(driver):
    try:
        assert ('https://identity.porsche.com/u/login/identifier?state'
                '=hKFo2SBSSXRfb3BmbWVvdWtjZ2JMOUtCWk9DSG5zcjJQTl85ZaFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIF9PMXBIMUMxamVWYTVQRllVZW9FQlZCcHo1T1hZanNjo2NpZNkgd01ZMTdNT1hZNHFCYUUyZnByYlY5VXQ0Zk1OM2hqR2w&ui_locales=en') in driver.current_url
        print("Test result: Page URL is: ", driver.current_url)
    except AssertionError:
        print("Test result: Page URL is different", driver.current_url)

def check_saved_searches_url(driver):
    try:
        assert "https://finder.porsche.com/us/en-US/saved-searches" in driver.current_url
        print("Test result: Page URL is: ", driver.current_url)
    except AssertionError:
        print("Test result: Page URL is different", driver.current_url)

def check_saved_cars_url(driver):
    try:
        assert "https://finder.porsche.com/us/en-US/favorites" in driver.current_url
        print("Test result: Page URL is: ", driver.current_url)
    except AssertionError:
        print("Test result: Page URL is different", driver.current_url)

def check_find_connect_services_url(driver):
    try:
        assert "https://connect-store.porsche.com/offer/us/en-US" in driver.current_url
        print("Test result: Page URL is: ", driver.current_url)
    except AssertionError:
        print("Test result: Page URL is different", driver.current_url)

def check_contact_and_support_url(driver):
    try:
        assert "https://ask.porsche.com/us/en-US" in driver.current_url
        print("Test result: Page URL is: ", driver.current_url)
    except AssertionError:
        print("Test result: Page URL is different", driver.current_url)

