import unittest
from base.base import Base
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time,os
from case.test_add_bug import ZandaoBug
from common.HTMLTestRunner import HTMLTestRunner


class Test01(unittest.TestCase):






    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html')
        self.driver.maximize_window()
        self.zan = ZandaoBug(self.driver)
        print('这是前置操作')

    def tearDown(self):
        self.driver.close()

    def test_01(self):
        bug_time = '这是测试bug标题' + time.strftime('-%Y_%m_%d_%H_%M_%S')

        self.zan.zandao_login()
        self.zan.add_bug(bug_time)
        result = self.zan.is_add_bug_success(bug_time)
        self.assertTrue(result)

    def test_02(self):
        bug_time = '这是测试bug标题11111' + time.strftime('-%Y_%m_%d_%H_%M_%S')

        self.zan.zandao_login()
        self.zan.add_bug(bug_time)
        result = self.zan.is_add_bug_success(bug_time)
        self.assertTrue(result)




