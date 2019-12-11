import unittest
import os
from common import HTMLTestRunner_cn


dis = unittest.defaultTestLoader.discover(os.getcwd(),'test_*.py')
print(dis)
print(os.getcwd())

reportPath = 'D:/Python_Project/selenium_JD/report/firstReport02.html'

f = open(reportPath,'wb')
run1 = HTMLTestRunner_cn.HTMLTestRunner(stream=f,title='first_report02',description='这是第一次自动化测试报告',retry=1)

run1.run(dis)

