from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html')

driver.find_element_by_id('account').send_keys('admin')
driver.find_element_by_name('password').send_keys('zq19941210@')
driver.find_element_by_id('submit').click()
driver.maximize_window()
text = driver.find_element_by_xpath('.//*[@class="user-name"]').text
print(text)


