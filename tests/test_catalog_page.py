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
