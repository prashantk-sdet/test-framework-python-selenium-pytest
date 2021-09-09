'''
Created on 08-Sep-2021

@author: prashantkumar
'''
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from pickle import TRUE
from testCases.conftest import setup

class Test_001_Login:
    baseUrl = "https://admin-demo.nopcommerce.com"
    username = "admin@yourstore.com"
    password = "admin"
    
    def test_homePageTitle(self, setup):
        self.driver = setup
        self.driver.get(Test_001_Login.baseUrl)
        actual_title = self.driver.title
        self.driver.close()
        if actual_title == "Your store. Login":
            assert TRUE
        else:
            assert False
    
    def test_Login(self, setup):
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

        
        
        