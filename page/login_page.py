#coding=utf-8
from base.base import Base
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

login_url ='http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html'
class LoginPage(Base):
    #登录元素
    loc_id = (By.ID, 'account')
    loc_pwd = (By.NAME, 'password')
    loc_login_btn = (By.ID, 'submit')
    loc_keep_login = (By.ID,'keepLoginon')
    loc_forget_pwd = (By.LINK_TEXT,'忘记密码')
    loc_admin = (By.CLASS_NAME,'user-name')
    #封装登录五种操作
    def input_id(self,text):
        self.sendKeys(self.loc_id,text)

    def input_password(self,text):
        self.sendKeys(self.loc_pwd,text)

    def click_login(self):
        self.click(self.loc_login_btn)

    def click_forget_pwd(self):
        self.click(self.loc_forget_pwd)

    def click_keep_login(self):
        self.click(self.loc_keep_login)

    #判断是否登录成功
    def get_username(self):
        try:
            ele = self.find_ele(self.loc_admin)


            return True
        except:
            return False

    #正常登录操作
    def login_succeess(self,id='admin',password='zq19941210@@'):
        self.driver.get(login_url)
        self.sendKeys(self.loc_id,id)
        self.sendKeys(self.loc_pwd,password)
        self.click(self.loc_login_btn)





if __name__=="__main__":
    driver = webdriver.Chrome()
    login_su = LoginPage(driver)
    login_su.login_succeess()

