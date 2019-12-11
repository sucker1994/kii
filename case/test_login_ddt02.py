import ddt
import unittest
from selenium import webdriver
from page.login_page import LoginPage


login_url ='http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html'

testdata=(
        {'username':'admin','password':'123456','expect':'admin'},
        {'username':'admin','password':'','expect':''},
        {'username':'admin111','password':'123456','expect':''},
)


@ddt.data
class TestLoginDdt(unittest.TestCase):




    def logon_ddt(self,username,password,expect):
        loginp = LoginPage(self.driver)
        loginp.input_id(username)
        loginp.input_password(password)
        loginp.click_login()
        result  = loginp.get_username()
        self.assertTrue(result)








    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(login_url)
        self.driver.maximize_window()

    def tearDown(self):
        print('houzhicaozuo')
    @ddt.data
    def test_login01(self,username,password,expect):
        data1 =testdata[0]
        print('打印测试数据%s'%data1)
        self.logon_ddt(data1['username'], data1['password'], data1['expect'])


    def test_login02(self,username,password,expect):
        data2 =testdata[1]
        print('打印测试数据%s' % data2)
        self.logon_ddt(data2['username'], data2['password'], data2['expect'])



    def test_login03(self,username,password,expect):
        data3 =testdata[2]
        print('打印测试数据%s' % data3)
        self.logon_ddt(data3['username'], data3['password'], data3['expect'])


if __name__=='__main__':
    unittest.main()


