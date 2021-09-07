'''
Created on 08-Sep-2021

@author: prashantkumar
'''
from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def setup():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver