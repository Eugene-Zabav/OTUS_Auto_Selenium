from selenium.webdriver.common.by import By


class AdminLoginPage:
    HEADING_AREA = (By.XPATH, "//*[@class='panel-heading']")
    LOGIN_TEXT_INPUT = (By.XPATH, "//input[@name='username']")
    PASSWORD_TEXT_INPUT = (By.XPATH, "//input[@name='password']")
    PASSWORD_RECOvERY_LINK = (By.XPATH, "//a[text()='Forgotten Password']")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
