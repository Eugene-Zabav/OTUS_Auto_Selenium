import pytest
import os.path
import logging
import datetime

import allure

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options as FFOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.safari.options import Options as SafariOption


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--max", action="store_true")
    parser.addoption("--headless", action="store_true")
    parser.addoption("--log_level", action="store_true", default="INFO")
    parser.addoption("--url", default="http://192.168.100.4:8081", help="Base application URL")


@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.outcome != "passed":
        item.status = "failed"
    else:
        item.status = "passed"

@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    log_level = request.config.getoption("--log_level")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)
    logger.info("===> Test %s started at %s" % (request.node.name, datetime.datetime.now()))

    if browser_name == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)
    elif browser_name == "safari":
        options = SafariOption()
        if headless:
            options.add_argument("--headless=new")
        driver = webdriver.Safari(options=options)
    elif browser_name == "firefox":
        options = FFOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
    elif browser_name == "yandex":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        service = Service(executable_path=os.path.expanduser("~/Documents/Python/drivers/yandexdriver"))
        driver = webdriver.Chrome(service=service, options=options)
    else:
        raise ValueError(f"Browser '{browser_name}' is not supported")

    if request.config.getoption("--max"):
        driver.maximize_window()

    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name

    logger.info("Browser %s started" % browser_name)

    def fin():
        if request.node.status == "failed":
            allure.attach(
                driver.get_screenshot_as_png(),
                name='failure_screenshot',
                attachment_type=allure.attachment_type.PNG
            )

        driver.quit()
        logger.info("===> Test %s finished at %s" % (request.node.name, datetime.datetime.now()))

    request.addfinalizer(fin)

    yield driver
