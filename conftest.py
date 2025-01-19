import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: '--browser_name=chrome' or '--browser_name=firefox'")

    parser.addoption('--language', action='store', default='en',
                     help="Choose language: '--language=en' or '--language=ru'")

@pytest.fixture
def browser(request):
    user_language = request.config.getoption('language')
    browser_name = request.config.getoption('browser_name')
    driver = None
    if browser_name in ['chrome', 'firefox']:
        if browser_name == 'chrome':
            options = Options()
            options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
            driver = webdriver.Chrome(options=options)
        else:
            options = webdriver.FirefoxOptions()
            options.set_preference("intl.accept_languages", user_language)
            driver = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield driver
    print("\nquit browser..")
    driver.quit()

