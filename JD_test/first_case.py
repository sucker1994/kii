#coding=utf-8
from selenium import webdriver
import time
import unittest

class FirstCase(unittest.TestCase):
    def test_case01(self):
        driver = webdriver.Chrome()
        driver.get('http://www.jd.com')

        time.sleep(3)
        driver.maximize_window()
        driver.find_element_by_class_name('link-login').click()
        driver.find_element_by_link_text('账户登录').click()
        username_ele = driver.find_element_by_xpath(".//*[@name='loginname']")

        self.assertTrue(username_ele)

if __name__=='__main()__':
    unittest.main()




