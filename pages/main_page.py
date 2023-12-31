import allure

from selenium.webdriver.common.by import By
from pages.elements.header_elemen import HeaderElements
from pages.base_page import BasePage


class MainPage(BasePage):
    PATH = ""
    ITEM_PRICE = (By.XPATH, "//p[@class='price']")
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[@type='button' and @onclick=\"cart.add('43');\"]")
    FIRST_FEATURED_ITEM_NAME = (By.XPATH, "//*[@id='content']//h4/a")
    CART = (By.XPATH, "//*[@id='cart-total']")
    ITEM_NAME_IN_CART = (By.XPATH, "//*[@id='cart']//td[2]")
    ITEMS_IN_CART = (By.XPATH, "//*[@id='cart']//td[3]")

    def open(self, url):
        with allure.step(f"Open '{url + self.PATH}' url"):
            self.logger.info(f"Open '{url + self.PATH}' url")
            self.browser.get(url + self.PATH)
            return self

    @allure.step("Change currency")
    def change_currency(self):
        self.logger.info("Change currency")
        HeaderElements(self.browser).change_currency_to_eur()
        return self

    @allure.step("Get price with current currency")
    def currency_price(self):
        self.logger.info("Get price with current currency")
        return self.element(self.ITEM_PRICE)

    @allure.step("Click 'Add to cart' button")
    def add_to_cart(self):
        self.logger.info("Click 'Add to cart' button")
        self.click(self.element(self.ADD_TO_CART_BUTTON))
        return self

    @allure.step("Click 'Cart' button")
    def click_cart_button(self):
        self.logger.info("Click 'Cart' button")
        self.click(self.element(self.CART))
        return self

    @allure.step("Check is item in cart")
    def item_in_cart(self):
        self.logger.info("Check is item in cart")
        return self.element(self.ITEMS_IN_CART)

    @allure.step("Get item name in cart")
    def item_in_cart_name(self):
        self.logger.info("Get item name in cart")
        return self.element(self.ITEM_NAME_IN_CART)

    @allure.step("Get first featured item name")
    def featured_item_name(self):
        self.logger.info("Get first featured item name")
        return self.element(self.FIRST_FEATURED_ITEM_NAME)
