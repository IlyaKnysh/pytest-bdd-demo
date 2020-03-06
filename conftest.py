import os
import shutil

import allure
import pytest
from selene.support.shared import browser
from selenium.common.exceptions import WebDriverException

from core.config import driver as driver_setup
from core.testlib.helpers.logger import logger
from core.testlib.helpers.utils import check_if_browser_log_has_errors


@pytest.yield_fixture(scope='function', autouse=True)
def driver(worker_id):
    logger.info(f'Starting driver for {worker_id}')
    ui_driver = driver_setup.Driver().start()
    browser.config.driver = ui_driver
    logger.info(f'Driver started for {worker_id}')

    yield

    try:
        ui_driver.quit()
    except WebDriverException:
        logger.info(f'Driver is already closed by exception interact hook')


@pytest.yield_fixture(scope='session', autouse=True)
def clean_reports():
    shutil.rmtree(browser.config.reports_folder, ignore_errors=True)
    try:
        os.makedirs(browser.config.reports_folder)
    except FileExistsError:
        pass


def pytest_exception_interact(node, call, report):
    """Attach screenshot if test failed"""
    if report.failed:
        try:
            check_if_browser_log_has_errors()
            with open(browser.config.last_screenshot, 'rb') as screen:
                allure.attach(screen.read(), 'screen', allure.attachment_type.PNG)

            browser.driver.quit()

        except Exception as ex:
            logger.error(ex)
