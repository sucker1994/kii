from selenium import webdriver
import time
from page.login_page import LoginPage


driver = webdriver.Chrome()
driver.get('http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html')
login = LoginPage(driver)
login.login_succeess()
time.sleep(3)
driver.get('http://127.0.0.1/zentao/bug-create-1-0-moduleID=0.html')
# js = 'document.getElementsByClassName("ke-edit-iframe")[0].contentWindow.document.body.innerHTML="hello"'
# driver.execute_script(js)
js2 = 'document.getElementById("tittle").value="这是bug标题";'
driver.execute_script(js2)







