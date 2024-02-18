import pytest
import logging
import datetime
import allure

from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FFOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--executor", action="store_true", default="192.168.100.4")
    parser.addoption("--remote", action="store_true")
    parser.addoption("--max", action="store_true")
    parser.addoption("--headless", action="store_true")
    parser.addoption("--log_level", action="store_true", default="INFO")
    parser.addoption("--url", default="http://192.168.100.2:8081", help="Base application URL")


@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
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

    remote = request.config.getoption("--remote")
    executor = request.config.getoption("--executor")
    executor_url = f"http://{executor}:4444/wd/hub"

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
        if remote:
            driver = webdriver.Remote(
                command_executor=executor_url,
                options=options
            )
        else:
            driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = FFOptions()
        if headless:
            options.add_argument("--headless")
        if remote:
            driver = webdriver.Remote(
                command_executor=executor_url,
                options=options
            )
        else:
            driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Browser '{browser_name}' is not supported")

    caps = {
        "browserName": browser_name
    }

    for k, v in caps.items():
        options.set_capability(k, v)

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
