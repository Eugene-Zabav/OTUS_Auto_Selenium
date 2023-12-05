from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert

class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait
        self.logger = browser.logger
        self.class_name = type(self).__name__

    def element(self, locator: tuple):
        self.logger.debug("%s: Find element by %s" % (self.class_name, locator))
        try:
            return WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Не дождался видимости элемента {locator}")

    def title(self, title_text: str):
        self.logger.debug("%s: Title text is '%s'" % (self.class_name, title_text))
        try:
            return WebDriverWait(self.browser, 2).until(EC.title_is(title_text))
        except TimeoutException:
            raise AssertionError(f"Title не '{title_text}'")

    def alert(self, locator: tuple, alert_text: str):
        self.logger.debug("%s: Alert text '%s' in alert %s" % (self.class_name, alert_text, locator))
        try:
            if WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(locator)).text != alert_text:
                raise AssertionError(f"Alert не '{alert_text}'")
            return WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Не дождался видимости элемента {locator}")

    def click(self, element):
        self.logger.debug("%s: Clicking element: %s" % (self.class_name, element))
        ActionChains(self.browser).move_to_element(element).pause(0.1).click().perform()

    def _input(self, element, value):
        self.logger.debug("%s: Input %s in input %s" % (self.class_name, value, element))
        self.click(element)
        element.clear()
        element.send_keys(value)

    def accept_browser_alert(self):
        self.logger.debug("%s: Accept browser alert" % (self.class_name))
        alert = Alert(self.browser)
        alert.accept()
