# selenium 是一个命令行指令做web自动化测试操作浏览器
# chromeDriver是一个第三方浏览器与selenium通信的桥接
# chromeDriver.exe放在python安装目录下的scripts目录下

from selenium import webdriver

chrome = webdriver.Chrome()

chrome.get('http://www.baidu.com')

# 仅仅截取当前屏幕的页面
chrome.save_screenshot('baidu.png')

html = chrome.page_source
print(html)

# chrome.quit()