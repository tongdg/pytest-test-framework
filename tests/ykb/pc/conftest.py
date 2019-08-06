"""Placeholder."""

# nothing here yet

from selenium import webdriver
import pytest
from common.utils import Utils
import random
utils = Utils()


@pytest.fixture(scope='function',params=('ie','chrome'),ids=('ie','chrome'))
def multi_browser_driver(request):
    # driver = webdriver.Chrome()
    driver = request.param
    if driver == 'chrome':
        driver = webdriver.Chrome()
    if driver == 'ie':
        driver = webdriver.Ie()
    yield driver
    driver.quit()




























