from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AdminPage(BasePage):
    PATH = "/admin"
    LOGIN_INPUT = (By.XPATH, "//input[@name='username']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    LOGOUT_BUTTON = (By.XPATH, "//*[contains(@class, 'hidden-xs')]/../..")

    def open(self, url):
        self.browser.get(url + self.PATH)
        return self

    def title_is_dashboard(self):
        self.title("Dashboard")
        return self

    def title_is_administration(self):
        self.title("Administration")
        return self

    def login(self, login, password):
        self._input(self.element(self.LOGIN_INPUT), login)
        self._input(self.element(self.PASSWORD_INPUT), password)
        self.click(self.element(self.LOGIN_BUTTON))
        return self

    def logout(self):
        self.element(self.LOGOUT_BUTTON).click()
        return self
