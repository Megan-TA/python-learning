from selenium import webdriver
from time import sleep

url = 'http://www.taobao.com'
driver = webdriver.Chrome()
driver.get(url)
# execute_script执行js代码
js = 'var a = document.documentElement.scrollTop = 100000'
driver.execute_script(js)

sleep(3)
