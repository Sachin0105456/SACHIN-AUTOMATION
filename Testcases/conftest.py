import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key

def pytest_addoption(parser):
    parser.addoption("--browser",action="store",default="chrome",help="specify the browser chrome or firefox or edge")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):
    # driver=webdriver.Chrome()
    # return driver
    global driver

    if browser=="chrome":
        driver=webdriver.Chrome()

    elif browser=="firefox":
        driver=webdriver.Firefox()

    elif browser=="edge":
        driver=webdriver.Edge()

    else:
        raise ValueError("Unsupported browser")

    return driver

def pytest_configure(config):
    config.stash[metadata_key] ['project Name'] = 'Ecommerce project, nopcommerce'
    config.stash[metadata_key] ['Test module Name'] = 'Admin login tests'
    config.stash[metadata_key] ['Tester Name'] = 'rohit'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('Plugins',None)