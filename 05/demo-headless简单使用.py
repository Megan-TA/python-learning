from selenium import webdriver

# 自动化测试提交搜索关键词
def chrome_test():
    chrome = webdriver.Chrome()
    chrome.get('https://www.baidu.com')
    chrome.find_element_by_id('kw').send_keys('python')
    chrome.find_element_by_id('su').click()

# 无头模式 不打开浏览器
def chrome_headless():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    chrome2 = webdriver.Chrome(chrome_options=options)
    chrome2.get('https://www.baidu.com')
    html = chrome2.page_source
    print(html)

chrome_headless()