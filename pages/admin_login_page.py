from selenium.webdriver.common.by import By


class AdminLoginPage:
    HEADING_AREA = (By.XPATH, "//*[@class='panel-heading']")
    LOGIN_INPUT = (By.XPATH, "//input[@name='username']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    PASSWORD_RECOVERY_LINK = (By.XPATH, "//a[text()='Forgotten Password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    HEADER = (By.XPATH, "//*[@id='content']//h1")
    LOGOUT_BUTTON = (By.XPATH, "//*[contains(@class, 'hidden-xs')]/../..")
