import allure

from selenium.webdriver.common.by import By
from pages.elements.header_elemen import HeaderElements
from pages.base_page import BasePage


class CatalogPage(BasePage):
    PATH = "/desktops"
    ITEM_PRICE = (By.XPATH, "//p[@class='price']")

    def open(self, url):
        with allure.step(f"Open '{url + self.PATH}' url"):
            self.logger.info(f"Open '{url + self.PATH}' url")
            self.browser.get(url + self.PATH)

    @allure.step("Change currency")
    def change_currency(self):
        self.logger.info("Change currency")
        HeaderElements(self.browser).change_currency_to_eur()
        return self

    @allure.step("Get price with current currency")
    def currency_price(self):
        self.logger.info("Get price with current currency")
        return self.element(self.ITEM_PRICE)
