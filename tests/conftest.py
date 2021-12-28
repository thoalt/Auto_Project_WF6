import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from pages.LoginPage import LoginPage
from utilites.handle_config import ConfigParserIni
from selenium.webdriver.remote.webdriver import WebDriver
import subprocess


@pytest.fixture(autouse=True, scope="class")
def setup(browser=None):
    # try:
    #     # Kill all process of chromedriver before create new
    #     subprocess.call("TASKKILL /f  /IM  CHROMEDRIVER.EXE")
    # except:
    #     pass

    if browser == "Chrome":
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif browser == "Firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser == "IE":
        driver = webdriver.Ie(executable_path=IEDriverManager().install())
    elif browser == "Edge":
        driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
    else:
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

    #driver.maximize_window()
    driver.implicitly_wait(10)
    return driver
    # request.cls.driver = driver# return driver
    # yield
    # driver.close()


@pytest.fixture(autouse=True, scope="class")
def login_webpage(request, setup):
    configInfo = ConfigParserIni.config_url_info()
    base_url = configInfo['base_url']
    username = configInfo['username']
    password = configInfo['password']
    driver: WebDriver = setup
    try:
        lp = LoginPage(driver)
        lp.open_url(base_url)
        lp.log_in_to_webgui(username, password)
        request.cls.driver = lp.driver
        yield
        driver.close()
    except Exception as exc:
        driver.quit()
        raise Exception("Login Failed!!!! \n" + str(exc))


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")


@pytest.fixture(scope="class", autouse=True)
def browser(request):
    """
    This function return the Browser value to setup method
    """
    return request.config.getoption("--browser")


@pytest.fixture(scope="class", autouse=True)
def url(request):
    """
    This function return the Browser value to setup method
    """
    return request.config.getoption("--url")
