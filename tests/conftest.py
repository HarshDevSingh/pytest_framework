import pytest
from selenium import webdriver
from webdriver_manager import chrome, firefox
from selenium.webdriver.chrome.service import Service
from tests.get_pages import Pages
import os
from utils.logging.Logger import Logger


@pytest.fixture(scope="class")
def load_generic_requirements(setup_driver, request):
    pages = Pages(request.cls.driver)
    request.cls.pages = pages
    request.cls.logger = Logger().logger()
    yield


def _get_driver_service(browser: str) -> Service:
    get_service = {
        "chrome": Service(chrome.ChromeDriverManager().install()),
        "firefox": Service(firefox.GeckoDriverManager().install())
    }
    return get_service.get(browser)


def _get_driver(browser: str):
    driver = {
        "chrome": webdriver.Chrome,
        "firefox": webdriver.Firefox
    }
    return driver.get(browser)(service=_get_driver_service(browser))


@pytest.fixture(params=[os.environ["BROWSER"]], scope="class")
def setup_driver(request):
    driver = _get_driver(request.param)
    if driver:
        request.cls.driver = driver
    else:
        raise Exception("unable to create/get driver")
    yield
    driver.close()
