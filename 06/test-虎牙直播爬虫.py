from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=options)
url = 'https://www.huya.com/g/lol'
driver.get(url)
html = driver.page_source
# 主播名称
names = driver.find_elements_by_xpath('//i[@class="nick"]')
# 正在观看人数
counts = driver.find_elements_by_xpath('//i[@class="js-num"]')

for name, count in zip(names, counts):
    print(name.text, ":", count.text)

if driver.page_source.find('laypage_next') != -1:
    # 下一页
    driver.find_element_by_xpath('//a[@class="laypage_next"]').click()