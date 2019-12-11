from selenium import webdriver
import time



driver = webdriver.Chrome()
driver.get('https://www.12306.cn/index/')
driver.maximize_window()
js= '''document.getElementById("train_date").removeAttribute("readonly");
       document.getElementById("train_date").value="2019-12-12"'''
driver.execute_script(js)
