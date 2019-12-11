import ddt
import unittest
from selenium import webdriver
from page.login_page import LoginPage
import time

login_url ='http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html'

# testdata=(
#         {'username':'admin','password':'123456','expect':'admin'},
#         {'username':'admin','password':'','expect':''},
#         {'username':'admin111','password':'123456','expect':''},
# )
testdata=[('admin','zq19941210@@','True'),
          ('admin11','zq19941210@@','False'),
          ('','zq19941210@@','False')
]
@ddt.ddt
class TestLoginDdt(unittest.TestCase):
    def login_ddt(self,username,password,expect):
        loginp = LoginPage(self.driver)
        loginp.input_id(username)
        loginp.input_password(password)
        loginp.click_login()
        time.sleep(5)
        re = loginp.get_username()
        self.assertTrue(re==expect)




    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(login_url)
        self.driver.maximize_window()

    def tearDown(self):
        print('houzhicaozuo')
        self.driver.close()

    @ddt.data(*testdata)
    def test_login01(self,data):

        # print('打印测试数据(%s,%s,%s)'%data1)
        self.login_ddt(data[0],data[1],data[2])






    # def test_login02(self):
    #     data2 =testdata[1]_______document.findElementsByClassName('ke')[0].contentWindow.document.body.innerHT
    #     # print('打印测试数据%s' % data2)
    #     self.login_ddt(data2[0],data2[1],data2[2])
    #
    #
    #
    # def test_login03(self):
    #     data3 =testdata[2]
    #     # print('打印测试数据%s' % data3)
    #     self.login_ddt(data3[0],data3[1],data3[2])


if __name__=='__main__':
    unittest.main()


