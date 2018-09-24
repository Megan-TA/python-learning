# get请求
# 处理get参数需要编码才能发送请求问题
from urllib.request import Request, urlopen
from urllib.parse import quote

# 原始地址：https://www.baidu.com/s?wd=get请求 无法直接百度直接发送请求
params = 'get请求'
url = 'https://www.baidu.com/s?wd={}'.format(quote(params))

print(quote(params))

userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'

headers = {
    'User-Agent': userAgent
}

request = Request(url, headers= headers)

res = urlopen(request)

print(res.read().decode())