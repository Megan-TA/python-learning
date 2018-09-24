# Request复杂请求
from urllib.request import urlopen, Request
from random import choices

url = 'https://www.cnblogs.com/it-tsz/p/9022456.html'

lists = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)'
]

# 自定义头文件用户信息
# 随机从头列表信息中取一个
headers = {
    'User-Agent': choices(lists)[0]
}

request = Request(url, headers = headers)

print(request.get_header('User-agent'))

res = urlopen(request)

print(res.read().decode())

