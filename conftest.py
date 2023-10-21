import pytest
import os.path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options as FFOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.safari.options import Options as SafariOption
import time


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--max", action="store_true")
    parser.addoption("--headless", action="store_true")
    parser.addoption("--url", default="http://192.168.100.4:8081/", help="Base application URL")


@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
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

    yield driver

    driver.quit()
