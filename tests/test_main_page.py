from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages import MainPage


def test_main_page_elements(browser, url):
    browser.get(url)

    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(MainPage.SHOPPING_CART_LINK))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(MainPage.SEARCH_TEXT_INPUT))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(MainPage.PRODUCT_IMAGE_SLIDER))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(MainPage.PRODUCTS_CARDS))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(MainPage.BRANDS_SLIDER))
