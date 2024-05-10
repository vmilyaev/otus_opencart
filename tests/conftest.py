import os.path
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options as FFOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--max", action="store_true")
    parser.addoption("--headless", action="store_true")


@pytest.fixture(scope="session")
def browser_name(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def browser(browser_name, request):
    headless = request.config.getoption("--headless")
    browser_name = request.config.getoption("--browser")
    if browser_name == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = FFOptions()
        if headless: options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
    elif browser_name == "yandex":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
            service = Service(
                executable_path=os.path.expanduser("~/drivers/yandexdriver-24.4.1.918-linux/yandexdriver"))
        driver = webdriver.Chrome(service=service, options=options)
    elif browser_name == "safari":
        driver = webdriver.Safari()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Browser {browser_name} not supported")
    if request.config.getoption("--max"):
        driver.maximize_window()

    yield driver

    time.sleep(1)
    driver.close()
