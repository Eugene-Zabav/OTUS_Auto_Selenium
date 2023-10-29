from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages import CatalogPage


def test_catalog_page_elements(browser, url):
    browser.get(url + "/desktops")

    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(CatalogPage.BREADCRUMB))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(CatalogPage.PRODUCTS_GROUP))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(CatalogPage.CATEGORY_DESCRIPTION))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(CatalogPage.POSITIONS_SORTING_DROPDOWN))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(CatalogPage.POSITIONS_SHOW_LIMIT_DROPDOWN))


def test_change_currency(browser, url):
    browser.get(url + "/desktops")

    default_usd_currency = WebDriverWait(browser, 1).until(EC.visibility_of_element_located(CatalogPage.ITEM_PRICE))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(CatalogPage.CURRENCY_DROP_DOWN)).click()
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(CatalogPage.CURRENCY_EUR)).click()
    changed_eur_currency = WebDriverWait(browser, 1).until(EC.visibility_of_element_located(CatalogPage.ITEM_PRICE))

    assert default_usd_currency != changed_eur_currency
