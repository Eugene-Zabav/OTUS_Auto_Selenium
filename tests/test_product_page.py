from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages import ProductPage


def test_product_page_elements(browser, url):
    browser.get(url + "/desktops/test")

    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(ProductPage.MAIN_PRODICT_IMAGE))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(ProductPage.NAVIGATION_TABS))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(ProductPage.PRODUCT_ACTION_BUTTONS))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(ProductPage.ADD_TO_CART_BUTTON))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(ProductPage.RELATED_PRODUCTS_AREA))
