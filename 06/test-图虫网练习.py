import requests
from fake_useragent import UserAgent
from lxml import etree

url = "https://tuchong.com/4235029/21115267/#image37487107"
headers = {
    "User-Agent": UserAgent().chrome
}

respone = requests.get(url, headers=headers)
e = etree.HTML(respone.text)
img_urls = e.xpath('//article[@class="post-content"]/img/@src')

for url in img_urls:
    # 请求的是图片
    res = requests.get(url, headers=headers)
    # print(url.rfind('/'))
    # rfind 从右向左查询第一个匹配的字符位置  : 代表匹配从当前位置到末尾的所有字符
    img_name = url[url.rfind('/') + 1:]
    with open('img/' + img_name, 'wb') as f:
        f.write(res.content)
