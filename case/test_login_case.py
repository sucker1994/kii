import unittest,time,os
from page.login_page import LoginPage
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from base.base import Base
from common.HTMLTestRunner_cn import HTMLTestRunner


class TestLoginCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html')
        self.driver.maximize_window()
        self.login = LoginPage(self.driver)

    def tearDown(self):
        pass

    def test01_right_login(self):
        self.login.input_id('admin')
        self.login.input_password('zq19941210@@')
        self.login.click_login()


        result = self.login.get_username()

        self.assertTrue(result=='admin')

    def test02_username_error(self):
        self.login.input_id('admin11')
        self.login.input_password('zq19941210@@')
        self.login.click_login()

        result = self.login.get_username()
        self.assertFalse(result)

    def test03_no_input(self):
        self.login.input_id('admin11')
        self.login.input_password('zq19941210@@')
        self.login.click_login()

        result = self.login.get_username()
        self.assertFalse(result)

    def test04_password_error(self):
        self.login.input_id('admin11')
        self.login.input_password('zq19941210')
        self.login.click_login()

        result = self.login.get_username()
        self.assertFalse(result)




if __name__=='__main__':
    file_path = 'D:/Python_Project/selenium_JD/report/firstReport03.html'
    print(file_path)

    f=open(file_path,'wb')
    discover_case = unittest.defaultTestLoader.discover(os.getcwd(),'test_login_z*.py')

    run11 = HTMLTestRunner(stream=f,title='登录模块测试报告',description='这是登录模块的测试')
    run11.run(discover_case)













