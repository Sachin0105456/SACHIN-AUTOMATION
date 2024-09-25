import time

import pytest
from selenium import webdriver
from pageobject.LoginPage import LoginPage
from utilities.readproperties import Readconfig
from utilities.customLogger import LogGen
from utilities import excelutils

class Test_001_Login:
    baseURL=Readconfig.getApplicationUrl()
    logger=LogGen.loggen()
    path=".//Testdata//admin_login_data.xlsx"
    status_list=[]


    def test_logindatadriven(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.rows=excelutils.get_row_count(self.path,"Sheet1")
        for r in range(2,self.rows+1):
            self.username=excelutils.read_data(self.path,"Sheet1",r,1)
            self.password=excelutils.read_data(self.path,"Sheet1",r,2)
            self.exp_login=excelutils.read_data(self.path,"Sheet1",r,3)
            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title=self.driver.title

            if act_title=="Dashboard / nopCommerce administration" and self.exp_login=="Yes":
                self.logger.info("test data is login")
                self.status_list.append("Pass")
                self.lp.clicklogout()
            elif act_title=="Dashboard / nopCommerce administration" and self.exp_login=="No":
                self.logger.info("test data is failed")
                self.driver.save_screenshot('C:/Users/Asus/PycharmProjects/nopcommerceaapp/Screenshots/test.png')
                self.status_list.append("Failed")
            elif act_title!="Dashboard / nopCommerce administration" and self.exp_login=="Yes":
                self.logger.info("Test case is failed")
                self.status_list.append("Failed")
            elif act_title!="Dashboard / nopCommerce administration" and self.exp_login=="No":
                self.logger.info("Test case is passed")
                self.status_list.append("Pass")

        print("status list is",self.status_list)

        if "Failed" in self.status_list:
            self.logger.info("Test admin data driven testcase is failed")
            assert False

        else:
            self.logger.info("Test admin data driven test is passed")
            assert True

