from selenium.webdriver.common.by import By


class MainPage:
    SHOPPING_CART_LINK = (By.XPATH, "//*[@title='Shopping Cart']")
    SEARCH_TEXT_INPUT = (By.XPATH, "//input[@name='search']")
    PRODUCT_IMAGE_SLIDER = (By.XPATH, "//*[@class='slideshow swiper-viewport']")
    PRODUCTS_CARDS = (By.XPATH, "(//*[contains(@class, 'row')])[3]")
    BRANDS_SLIDER = (By.XPATH, "//*[@class='carousel swiper-viewport']")
