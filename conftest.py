from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


def pytest_addoption(parser):
    parser.addoption('--language')

@pytest.fixture(scope="function")
def browser(request):
    browser_lang = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': browser_lang})
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    yield browser
    browser.quit()