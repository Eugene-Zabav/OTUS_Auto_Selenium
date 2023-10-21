from selenium.webdriver.common.by import By


class MainPage:
    SHOPPING_CART_LINK = (By.XPATH, "//*[@title='Shopping Cart']")
    SEARCH_TEXT_INPUT = (By.XPATH, "//input[@name='search']")
    PRODUCT_IMAGE_SLIDER = (By.XPATH, "//*[@class='slideshow swiper-viewport']")
    PRODUCTS_CARDS = (By.XPATH, "(//*[contains(@class, 'row')])[3]")
    BRANDS_SLIDER = (By.XPATH, "//*[@class='carousel swiper-viewport']")
    CURRENCY_DROP_DOWN = (By.XPATH, "//*[@class='btn btn-link dropdown-toggle']")
    CURRENCY_EUR = (By.XPATH, "//*[@name='EUR']")
    ITEM_PRICE = (By.XPATH, "//p[@class='price']")
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[@type='button' and @onclick=\"cart.add('43');\"]")
    CART = (By.XPATH, "//*[@id='cart-total']")
    ITEM_NAME_IN_CART = (By.XPATH, "//*[@id='cart']//td[2]")
    ITEMS_IN_CART = (By.XPATH, "//*[@id='cart']//td[3]")
