from selenium import webdriver
import time

#打开京东页面并最大化页面
driver = webdriver.Chrome()
driver.get('http://www.jd.com')

time.sleep(5)
driver.maximize_window()

# h1 = driver.current_window_handle
# all = driver.window_handles
# print(h1,all)
driver.find_element_by_class_name('link-login').click()
driver.find_element_by_link_text('账户登录').click()
driver.find_element_by_xpath(".//*[@name='loginname']").send_keys('17853977760')
driver.find_element_by_xpath(".//*[@name='nloginpwd']").send_keys('zq19941210@')
driver.find_element_by_xpath(".//*[@class='btn-img btn-entry']").click()





# driver.find_elements_by_id('loginname').send_keys('17853977760')
# driver.find_elements_by_id('nloginpwd').send_keys('zq19941210@')
# driver.find_element_by_class_name('btn-img btn-entry').click()
# # driver.close()



