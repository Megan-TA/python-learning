import requests
from fake_useragent import UserAgent

headers = {
    "User-Agent": UserAgent().chrome`1
}

baidu_url = 'https://www.baidu.com'

res = requests.get(baidu_url, headers = headers)
res.encoding = 'utf-8'
print(res.text)
# 代理
proxy_url = 'http://httpbin.org/get'

proxies = {
    "http": "http://118.190.95.43:9001"
}
res = requests.get(proxy_url, headers = headers, proxies = proxies)
print(res.text)
# session
# 保留session
session = requests.session()
# res = session.get()
# res2 = session.post()

