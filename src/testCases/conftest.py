'''
Created on 08-Sep-2021

@author: prashantkumar
'''
from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from utilities import XLUtils

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser == 'ie':
        driver = webdriver.Ie(executable_path=IEDriverManager().install())
    elif browser == 'edge':
        driver = webdriver.Ie(EdgeChromiumDriverManager().install())
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")
    
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

# Pytest html report
# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Prashant - nop Commerse'
    config._metadata['Module Name'] = 'Login'
    config._metadata['Tester'] = 'Prashant Kumar'
   
# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook()
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


    