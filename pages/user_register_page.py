from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class UserRegisterPage(BasePage):
    PATH = "/index.php?route=account/register"
    FIRST_NAME_TEXT_INPUT = (By.XPATH, "//input[@name='firstname']")
    LAST_NAME_TEXT_INPUT = (By.XPATH, "//input[@name='lastname']")
    EMAIL_TEXT_INPUT = (By.XPATH, "//input[@name='email']")
    PHONE_TEXT_INPUT = (By.XPATH, "//input[@name='telephone']")
    PASSWORD_TEXT_INPUT = (By.XPATH, "//input[@name='password']")
    PASSWORD_CONFIRM_TEXT_INPUT = (By.XPATH, "//input[@name='confirm']")
    POLICY_AGREE_CHECKBOX = (By.XPATH, "//input[@type='checkbox']")
    CONTINUE_SUBMIT_BUTTON = (By.XPATH, "//input[@type='submit']")

    def open(self, url):
        self.browser.get(url + self.PATH)
        return self

    def register_new_user(self, first_name, last_name, email, phone, password, confirm_password):
        self._input(self.element(self.FIRST_NAME_TEXT_INPUT), first_name)
        self._input(self.element(self.LAST_NAME_TEXT_INPUT), last_name)
        self._input(self.element(self.EMAIL_TEXT_INPUT), email)
        self._input(self.element(self.PHONE_TEXT_INPUT), phone)
        self._input(self.element(self.PASSWORD_TEXT_INPUT), password)
        self._input(self.element(self.PASSWORD_CONFIRM_TEXT_INPUT), confirm_password)
        self.click(self.element(self.POLICY_AGREE_CHECKBOX))
        self.click(self.element(self.CONTINUE_SUBMIT_BUTTON))
        return self

    def title_is_success(self):
        self.title("Your Account Has Been Created!")
        return self
