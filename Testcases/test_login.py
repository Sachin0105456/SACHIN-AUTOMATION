import pytest
from selenium import webdriver
from pageobject.LoginPage import LoginPage
from utilities.readproperties import Readconfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL=Readconfig.getApplicationUrl()
    username=Readconfig.getUsername()
    password=Readconfig.getPassword()
    logger=LogGen.loggen()

    def test_homePageTitle(self,setup):
        self.logger.info("*********Test_001_login title page *********************8")
        self.driver=setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title

        if act_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("*********Homepage Title test is passed ************************")
        else:
            self.logger.info("**********Homepage Title test is not pasesd but failed *****************")
            assert False


    def test_login(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title

        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot('C:/Users/Asus/PycharmProjects/nopcommerceaapp/Screenshots/test.png')
            assert False

