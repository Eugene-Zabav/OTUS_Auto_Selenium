from selenium.webdriver.common.by import By
from pages.elements.header_elemen import HeaderElements
from pages.base_page import BasePage


class CatalogPage(BasePage):
    PATH = "/desktops"
    ITEM_PRICE = (By.XPATH, "//p[@class='price']")

    def open(self, url):
        self.browser.get(url + self.PATH)

    def change_currency(self):
        HeaderElements(self.browser).change_currency_to_eur()
        return self

    def currency_price(self):
        return self.element(self.ITEM_PRICE)
