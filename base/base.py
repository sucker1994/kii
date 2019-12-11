#coding=utf-8
#封装基础方法
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select



class Base():
    def __init__(self,driver):
        self.driver = driver
        self.timeout = 10
        self.time = 0.5

    def is_title(self,_title):
        ele = WebDriverWait(self.driver, self.timeout, self.time).until(EC.title_is(_title))
        return ele

    def is_title_contains(self,_title):
        ele = WebDriverWait(self.driver, self.timeout, self.time).until(EC.title_contains(_title))
        return ele

    def is_text_in_element(self,locator,_text):
        ele = WebDriverWait(self.driver, self.timeout, self.time).until(EC.text_to_be_present_in_element(locator,_text))
        return ele

    #查找元素操作
    def find_ele(self,locator):
        ele=WebDriverWait(self.driver,self.timeout,self.time).until(lambda driver:driver.find_element(*locator))
        return ele



    def findElementNew(self,locator):
        ele=WebDriverWait(self.driver,self.timeout,self.time).until(EC.presence_of_element_located(locator))
        return ele

    def is_alert(self):
        try:
            ele = WebDriverWait(self.driver, self.timeout, self.time).until(EC.alert_is_present())
            return ele
        except:
            return False

    #判断是否有value值
    def is_value_in_element(self,locator,_value):
        try:
            ele=WebDriverWait(self.driver,self.timeout,self.time).until(EC.text_to_be_present_in_element_value(locator,_value))
            return ele
        except:
            return False


        # 查找元素操作
    def find_eles(self, locator):
        eles = WebDriverWait(self.driver, self.timeout, self.time).until(
            lambda driver: driver.find_elements(*locator))
        return eles
    #输入文本操作
    def sendKeys(self,locator,text):
        self.find_ele(locator).send_keys(text)
    #点击元素操作
    def click(self,locator):
        ele01 = self.find_ele(locator)
        ele01.click()
    #清空输入框
    def clear(self,locator):
        self.find_ele(locator).clear()


    #鼠标悬停
    def move_to_element(self,locator):
        ele = self.find_ele(locator)
        ActionChains(driver).move_to_element(ele).perform()

    ''' 封装三种select方法 '''
    def select_by_index(self,locator,index=0):
        element = self.find_ele(locator)
        Select(element).select_by_index(index)

    def select_by_value(self,locator,value):
        element = self.find_ele(locator)
        Select(element).select_by_value(value)

    def select_by_text(self,locator,text):
        element = self.find_ele(locator)
        Select(element).deselect_by_visible_text(text)

    #封装三种滚动条滑动的操作
    def js_focus_element(self,locator):
        target = self.find_ele(locator)
        self.driver.execute_script('arguments[0].scrollIntoView()',target)

    def js_scroll_top(self):
        js = 'windows.scrollTo(0,0)'
        self.driver.execute_script(js)

    def js_scroll_end(self):
        js = 'windows.scrollTo(0,document.body.scrollHeight)'
        self.driver.execute_script(js)








if __name__=='__main__':
    driver = webdriver.Chrome()
    driver.get('http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html')
    driver.maximize_window()
    ele1=Base(driver)
    loc1 = (By.ID,'account')
    loc2 = (By.NAME,'password')
    loc3 = (By.ID,'submit')
    # ele1.sendKeys(loc1,'admin')
    # ele1.sendKeys(loc2,'zq19941210@')
    # ele1.click(loc3)
    # result = ele1.is_title('用户登录 - 禅道')
    # print(result)
    # print(ele1.is_title_contains('禅道'))
    # re = ele1.is_text_in_element((By.LINK_TEXT,'忘记密码'),'忘记密码')
    # print(re)
    re = ele1.is_alert()
    print(re)

    ele1.sendKeys(loc1,'admin')
    ele1.sendKeys(loc2,'123444')
    ele1.click(loc3)
    re2 = ele1.is_alert()
    print(re2)
    print(re2.text)






