#coding=utf-8
from base.base import Base
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

class ZandaoBug(Base):
    #登录定位
    loc1 = (By.ID, 'account')
    loc2 = (By.NAME, 'password')
    loc3 = (By.ID, 'submit')

    #添加bug定位
    loc_test = (By.LINK_TEXT,'测试')
    loc_bug = (By.XPATH,'.//*[@data-id="bug"]')
    loc_add_bug = (By.XPATH,'.//a[contains(@href,"bug-create")]')
    loc_version = (By.XPATH, './/*[@class="chosen-choices"]')
    loc_zhugan = (By.CLASS_NAME,'active-result')
    loc_input_title = (By.NAME,'title')
    loc_input_body = (By.CLASS_NAME,'article-content')
    loc_submit = (By.ID,'submit')

    loc_new = (By.XPATH,'.//*[@id="bugList"]/tbody/tr[1]/td[5]')
    loc_admin=(By.CLASS_NAME,'user-name')



    def __init__(self,driver:webdriver.Chrome):
        self.driver = driver
        self.timeout = 10
        self.time = 0.5





    #登录
    def zandao_login(self,username='admin',password='zq19941210@@'):
        self.sendKeys(self.loc1,username)
        self.sendKeys(self.loc2,password)
        self.click(self.loc3)

    #添加bug
    def add_bug(self,title,text='11111'):

        self.click(self.loc_test)
        self.click(self.loc_bug)
        self.click(self.loc_add_bug)
        self.click(self.loc_version)
        self.click(self.loc_zhugan)

        self.sendKeys(self.loc_input_title,title)
        frame = self.driver.find_element_by_class_name('ke-edit-iframe')

        self.driver.switch_to.frame(frame)
        self.sendKeys(self.loc_input_body,text)
        self.driver.switch_to.default_content()
        # self.driver.find_element_by_id('submit').click()
        # print(self.loc_submit)
        # print(self.loc_submit.location)
        y = self.driver.find_element_by_id('submit').location
        # print(self.drivloc_submit.location)
        loc_y = y['y']


        self.driver.execute_script("window.scrollTo(0, %s)"%loc_y)
        time.sleep(3)
        self.driver.find_element_by_id('submit').click()
        time.sleep(3)




    def is_add_bug_success(self,_text):
        return self.is_text_in_element(self.loc_new,_text)

    def get_username(self,loc):
        try:
            text = self.find_ele(loc).text
            # ('.//*[@class="user-name"]').text
            print(text)

        except:
            return False




if __name__=='__main__':
    driver = webdriver.Chrome()
    driver.get('http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html')
    driver.maximize_window()
    bug_time = '这是测试bug标题'+time.strftime('-%Y_%m_%d_%H_%M_%S')
    zan=ZandaoBug(driver)
    zan.zandao_login()
    result = zan.get_username(zan.loc_admin)
    print(result)
    # zan.add_bug(bug_time)
    # result = zan.is_add_bug_success(bug_time)
    # print(result)

