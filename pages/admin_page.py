from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AdminPage(BasePage):
    PATH = "/admin"
    LOGIN_INPUT = (By.XPATH, "//input[@name='username']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    LOGOUT_BUTTON = (By.XPATH, "//*[contains(@class, 'hidden-xs')]/../..")
    ADD_NEW_PRODUCT_BUTTON = (By.XPATH, "//*[@data-original-title='Add New']")
    CATALOG_LEFT_TAB = (By.XPATH, "//*[@id='menu-catalog']")
    PRODUCTS_LEFT_TAB = (By.XPATH, "//*[@id='collapse1']/li[2]")
    PRODUCT_NAME_INPUT = (By.XPATH, "//input[@id='input-name1']")
    META_TAG_TITLE_INPUT = (By.XPATH, "//input[@id='input-meta-title1']")
    DATA_TAB = (By.XPATH, "//*[@id='form-product']/ul/li[2]")
    MODEL_INPUT = (By.XPATH, "//input[@id='input-model']")
    SAVE_NEW_PRODUCT_BUTTON = (By.XPATH, "//*[@data-original-title='Save']")
    DELETE_SELECTED_PRODUCT_BUTTON = (By.XPATH, "//*[@data-original-title='Delete']")
    SUCCESS_ALERT = (By.XPATH, "//*[contains(@class, 'alert-success alert-dismissible')]")
    TEST_PRODUCT_CHECKBOX = (By.XPATH, "//*[contains(text(), 'TestProduct')]/preceding-sibling::td/input[@type='checkbox']")


    def open(self, url):
        self.logger.info(f"open '{url + self.PATH}' url")
        self.browser.get(url + self.PATH)
        return self

    def title_is_dashboard(self):
        self.logger.info("Title is 'Dashboard'")
        self.title("Dashboard")
        return self

    def title_is_administration(self):
        self.logger.info("Title is 'Administration'")
        self.title("Administration")
        return self

    def login(self, login, password):
        self.logger.info(f"logining by Login={login} Password={password}")
        self._input(self.element(self.LOGIN_INPUT), login)
        self._input(self.element(self.PASSWORD_INPUT), password)
        self.click(self.element(self.LOGIN_BUTTON))
        return self

    def logout(self):
        self.logger.info(f"Click LOGOUT button")
        self.click(self.element(self.LOGOUT_BUTTON))
        return self

    def create_default_product(self):
        self.logger.info(f"Creating default product")
        self.click(self.element(self.CATALOG_LEFT_TAB))
        self.click(self.element(self.PRODUCTS_LEFT_TAB))
        self.click(self.element(self.ADD_NEW_PRODUCT_BUTTON))
        self._input(self.element(self.PRODUCT_NAME_INPUT), "TestProduct")
        self._input(self.element(self.META_TAG_TITLE_INPUT), "TstsMetaTag")
        self.click(self.element(self.DATA_TAB))
        self._input(self.element(self.MODEL_INPUT), "TestModel")
        self.click(self.element(self.SAVE_NEW_PRODUCT_BUTTON))
        return self

    def delete_default_product(self):
        self.logger.info(f"Deleting default product")
        self.click(self.element(self.CATALOG_LEFT_TAB))
        self.click(self.element(self.PRODUCTS_LEFT_TAB))
        self.click(self.element(self.TEST_PRODUCT_CHECKBOX))
        self.click(self.element(self.DELETE_SELECTED_PRODUCT_BUTTON))
        return self


    def show_success_alert(self):
        self.logger.info(f"Show success alert")
        self.alert(self.SUCCESS_ALERT, "Success: You have modified products!\n×")
        return self
