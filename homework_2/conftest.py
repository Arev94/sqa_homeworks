import pytest
from selenium import webdriver
from wait.wait import Wait


@pytest.fixture(scope='class')
def get_driver(request):
    browser_type: str = request.config.getoption("--browser")
    if browser_type.lower() == 'chrome':
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
    get_wait = Wait(driver)
    driver.get("https://opensource-demo.orangehrmlive.com")

    request.cls.driver = driver
    request.cls.get_wait = get_wait

    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")