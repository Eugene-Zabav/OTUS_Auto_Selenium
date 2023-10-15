from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages import UserRegisterPage


def test_user_register_page_elements(browser, url):
    browser.get(url + "/index.php?route=account/register")

    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(UserRegisterPage.LOGIN_PAGE_LINK))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(UserRegisterPage.FIRST_NAME_TEXT_INPUT))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(UserRegisterPage.USER_NAVIGATION_AREA))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(UserRegisterPage.PRIVACY_POLICY_LINK))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(UserRegisterPage.CONTINUE_SUBMIT_BUTTON))
