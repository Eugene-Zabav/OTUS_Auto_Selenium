from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages import AdminLoginPage


def test_admin_login_page_elements(browser, url):
    browser.get(url + "/admin")

    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(AdminLoginPage.HEADING_AREA))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(AdminLoginPage.LOGIN_INPUT))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(AdminLoginPage.PASSWORD_INPUT))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(AdminLoginPage.PASSWORD_RECOVERY_LINK))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(AdminLoginPage.LOGIN_BUTTON))


def test_admin_login_logout(browser, url):
    browser.get(url + "/admin")

    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(AdminLoginPage.LOGIN_INPUT)).send_keys("user")
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(AdminLoginPage.PASSWORD_INPUT)).send_keys("bitnami")
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(AdminLoginPage.LOGIN_BUTTON)).click()
    WebDriverWait(browser, 1).until(EC.title_is("Dashboard"))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(AdminLoginPage.LOGOUT_BUTTON)).click()
    WebDriverWait(browser, 1).until(EC.title_is("Administration"))
