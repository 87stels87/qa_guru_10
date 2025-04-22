import pytest

from selene import browser


@pytest.fixture(scope='session')
def browser_setup():
    browser.driver.maximize_window()
    yield
    browser.quit()
