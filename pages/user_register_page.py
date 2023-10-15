from selenium.webdriver.common.by import By


class UserRegisterPage:
    LOGIN_PAGE_LINK = (By.XPATH, "//a[text()='login page']")
    FIRST_NAME_TEXT_INPUT = (By.XPATH, "//input[@name='firstname']")
    USER_NAVIGATION_AREA = (By.XPATH, "//*[@class='list-group']")
    PRIVACY_POLICY_LINK = (By.XPATH, "//a[@class='agree']")
    CONTINUE_SUBMIT_BUTTON = (By.XPATH, "//input[@type='submit']")
