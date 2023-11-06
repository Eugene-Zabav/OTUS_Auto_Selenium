from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HeaderElements(BasePage):
    CURRENCY_DROP_DOWN = (By.XPATH, "//*[@class='btn btn-link dropdown-toggle']")
    CURRENCY_EUR = (By.XPATH, "//*[@name='EUR']")

    def change_currency_to_eur(self):
        self.click(self.element(self.CURRENCY_DROP_DOWN))
        self.click(self.element(self.CURRENCY_EUR))
