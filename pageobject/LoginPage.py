from selenium.webdriver.common.by import By
class LoginPage:
    textbox_username_id="Email"
    textbox_password_id="Password"
    button_login_xpath="//button[contains(text(),'Log in')]"
    link_logout_linktext="Logout"


    def __init__(self, driver):
        self.driver=driver

    def setUserName(self, username):
       self.driver.implicitly_wait(5)
       self.driver.find_element(By.ID,self.textbox_username_id).clear()
       self.driver.find_element(By.ID,self.textbox_username_id).send_keys(username)


    def setPassword(self, password):
        self.driver.find_element(By.ID,'Password').clear()
        self.driver.find_element(By.ID,'Password').send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,"//button[contains(text(),'Log in')]").click()

    def clicklogout(self):
        self.driver.find_element(By.LINK_TEXT,'Logout').click()

