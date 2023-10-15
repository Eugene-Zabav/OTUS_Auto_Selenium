from selenium.webdriver.common.by import By


class ProductPage:
    MAIN_PRODICT_IMAGE = (By.XPATH, "//*[@class='thumbnail']")
    NAVIGATION_TABS = (By.XPATH, "//*[@class='nav nav-tabs']")
    PRODUCT_ACTION_BUTTONS = (By.XPATH, "//*[@class='btn-group']")
    ADD_TO_CART_BUTTON = (By.XPATH, "//*[@id='button-cart']")
    RELATED_PRODUCTS_AREA = (By.XPATH, "(//*[contains(@class, 'row')])[4]")
