'''
Created on 08-Sep-2021

@author: prashantkumar
'''
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from pickle import TRUE
from testCases.conftest import setup
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseUrl = ReadConfig.getConfigValue("baseUrl")
    username = ReadConfig.getConfigValue("username")
    password = ReadConfig.getConfigValue("password")
    logger = LogGen.loggen()
    
    @pytest.mark.sanity
    def test_homePageTitle(self, setup):
        self.logger.info("Starting test_homePageTitle")
        self.driver = setup
        self.driver.get(Test_001_Login.baseUrl)
        actual_title = self.driver.title
        if actual_title == "Your store. Login":
            assert TRUE
            self.driver.close()
        else:
            self.driver.save_screenshot("screenshots/test_homePageTitle.png")
            self.driver.close()
            assert False
    
    @pytest.mark.regression
    def test_Login(self, setup):
        self.logger.info("Starting test_Login")
        self.driver = setup
        self.driver.get(Test_001_Login.baseUrl)
        self.loginPage = LoginPage(self.driver)
        self.loginPage.setUserName(Test_001_Login.username)
        self.loginPage.setPassword(Test_001_Login.password)
        self.loginPage.clickLogin()
        actual_title = self.driver.title
        if actual_title == "Dashboard / nopCommerce administration":
            assert TRUE
        else:
            assert False
        self.loginPage.clickLogout()
        self.driver.close()

        
        
        