from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_main_page_elements(browser, url):
    browser.get(url)
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, "//*[@title='Shopping Cart']")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='search']")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, "//*[@class='slideshow swiper-viewport']")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, "(//*[contains(@class, 'row')])[3]")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, "//*[@class='carousel swiper-viewport']")))


def test_catalog_page_elements(browser, url):
    browser.get(url + "/desktops")
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, "//*[@class='breadcrumb']")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, "//*[@class='list-group']")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, "(//*[contains(@class, 'row')])[3]")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='input-sort']")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='input-limit']")))


def test_product_page_elements(browser, url):
    browser.get(url + "/desktops/test")
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, "//*[@class='thumbnail']")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, "//*[@class='nav nav-tabs']")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, "//*[@class='btn-group']")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='button-cart']")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, "(//*[contains(@class, 'row')])[4]")))


def test_admin_login_page_elements(browser, url):
    browser.get(url + "/admin")

    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, "//*[@class='panel-heading']")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='username']")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='password']")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Forgotten Password']")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))


def test_user_register_page_elements(browser, url):
    browser.get(url + "/index.php?route=account/register")

    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='login page']")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='firstname']")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, "//*[@class='list-group']")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, "//a[@class='agree']")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, "//input[@type='submit']")))

