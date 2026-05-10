import pytest
import allure

from selenium import webdriver
from selenium.webdriver.edge.options import Options


@pytest.fixture
def driver():

    options = Options()

    driver = webdriver.Edge(options=options)

    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs["driver"]

        screenshot = driver.get_screenshot_as_png()

        allure.attach(
            screenshot,
            name="Failure Screenshot",
            attachment_type=allure.attachment_type.PNG
        )