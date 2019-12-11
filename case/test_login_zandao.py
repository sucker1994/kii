import unittest,time
from selenium import webdriver

class ZandaoTest(unittest.TestCase):
    def get_username(self):
        try:
            text=self.driver.find_element_by_xpath('.//*[@class="user-name"]').text
            return text
        except:
            return ''


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html')
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()
        self.driver.close()



    def test_01(self):
        time.sleep(3)
        self.driver.find_element_by_id('account').send_keys('admin')
        self.driver.find_element_by_name('password').send_keys('z111q19941210@')
        self.driver.find_element_by_id('submit').click()
        time.sleep(3)
        t = self.get_username()

        self.assertTrue(t=='admin')




    def is_alert_exist(self):
        try:
            alert = self.driver.switch_to_alert()
            text = alert.text
            alert.accept()
            return text
        except:
            return ''

    def test_02(self):
        self.driver.find_element_by_id('account').send_keys('adminaaa')
        self.driver.find_element_by_name('password').send_keys('zq1994')
        self.driver.find_element_by_id('submit').click()
        time.sleep(3)

        t=self.is_alert_exist()
        self.assertTrue(t!='')



if __name__=='__main__':
    unittest.main()






