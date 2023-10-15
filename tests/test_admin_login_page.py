from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages import AdminLoginPage


def test_admin_login_page_elements(browser, url):
    browser.get(url + "/admin")

    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(AdminLoginPage.HEADING_AREA))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(AdminLoginPage.LOGIN_TEXT_INPUT))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(AdminLoginPage.PASSWORD_TEXT_INPUT))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(AdminLoginPage.PASSWORD_RECOvERY_LINK))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(AdminLoginPage.LOGIN_SUBMIT_BUTTON))
