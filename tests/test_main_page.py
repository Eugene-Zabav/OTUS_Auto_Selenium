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


def test_change_currency(browser, url):
    browser.get(url)

    default_usd_currency = WebDriverWait(browser, 1).until(EC.visibility_of_element_located(MainPage.ITEM_PRICE))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(MainPage.CURRENCY_DROP_DOWN)).click()
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(MainPage.CURRENCY_EUR)).click()
    changed_eur_currency = WebDriverWait(browser, 1).until(EC.visibility_of_element_located(MainPage.ITEM_PRICE))

    assert default_usd_currency != changed_eur_currency


def test_add_item_to_cart(browser, url):
    browser.get(url)

    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(MainPage.ADD_TO_CART_BUTTON)).click()
    cart_button = WebDriverWait(browser, 1).until(EC.visibility_of_element_located(MainPage.CART))

    assert cart_button.text.startswith("1 item(s) - ")

    cart_button.click()
    items_in_cart = WebDriverWait(browser, 1).until(EC.visibility_of_element_located(MainPage.ITEMS_IN_CART))
    item_name = WebDriverWait(browser, 1).until(EC.visibility_of_element_located(MainPage.ITEM_NAME_IN_CART))

    assert item_name.text == "MacBook"
    assert items_in_cart.text == "x 1"
