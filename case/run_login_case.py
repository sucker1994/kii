import os

from common.HTMLTestRunner_cn import HTMLTestRunner
import unittest

file_path = 'D:/Python_Project/selenium_JD/report/firstReport03.html'
print(file_path)

f=open(file_path,'wb')
discover_case = unittest.defaultTestLoader.discover(os.getcwd(),'test_login_*.py')

run11 = HTMLTestRunner(stream=f,title='登录模块测试报告',description='这是登录模块的测试')
run11.run(discover_case)

