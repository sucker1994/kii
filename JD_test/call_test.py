from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html')


# r = EC.title_is('百度一下，你就知道')(driver)
# print(r)
# assert r
#
# r2 = EC.title_contains('1百度一下')(driver)
# print(r2)
# assert r2


loc1=('xpath','.//*[text()="忘记密码"]')

l=EC.presence_of_element_located(loc1)(driver)
print(l)
assert l