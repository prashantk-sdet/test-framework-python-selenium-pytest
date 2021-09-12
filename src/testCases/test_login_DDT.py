'''
Created on 08-Sep-2021

@author: prashantkumar
'''
import pytest
import time
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from pickle import TRUE, FALSE
from testCases.conftest import setup
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils


def get_data(path):
    testData = []
    rows = XLUtils.getRowCount(path, "Sheet1")
        
    for r in range(2, rows+1):
        username = XLUtils.readData(path, "Sheet1", r, 1)
        password = XLUtils.readData(path, "Sheet1", r, 2)
        exp = XLUtils.readData(path, "Sheet1", r, 3)
        testData.append((username, password, exp))
    print("*" * 80)
    print(testData)
    return testData

class Test_002_DDT_Login:
    baseUrl = ReadConfig.getConfigValue("baseUrl")
    path = "testData/LoginData.xlsx"
    logger = LogGen.loggen()
    testData = get_data(path)

    @pytest.mark.parametrize("username, password, exp", testData)
    def test_Login_DDT(self, setup, username, password, exp):
        print(username, password, exp)
        self.logger.info("****** Starting test_Login_DDT ******")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.loginPage = LoginPage(self.driver)
        self.loginPage.setUserName(username)
        self.loginPage.setPassword(password)
        self.loginPage.clickLogin()
        time.sleep(5)
        actual_title = self.driver.title
        exp_title = "Dashboard / nopCommerce administration"
        if exp == "pass":
            if actual_title == exp_title:
                assert True
                self.loginPage.clickLogout()
            else:
                assert False
        else:
            if actual_title != exp_title:
                assert True
            else:
                assert False
                self.loginPage.clickLogout()
        self.driver.close()

        
        
        