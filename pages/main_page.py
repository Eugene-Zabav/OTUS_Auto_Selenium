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
        self.browser.get(url + self.PATH)
        return self

    def change_currency(self):
        HeaderElements(self.browser).change_currency_to_eur()
        return self

    def currency_price(self):
        return self.element(self.ITEM_PRICE)

    def add_to_cart(self):
        self.click(self.element(self.ADD_TO_CART_BUTTON))
        return self

    def click_cart_button(self):
        self.click(self.element(self.CART))
        return self

    def item_in_cart(self):
        return self.element(self.ITEMS_IN_CART)

    def item_in_cart_name(self):
        return self.element(self.ITEM_NAME_IN_CART)

    def featured_item_name(self):
        return self.element(self.FIRST_FEATURED_ITEM_NAME)
