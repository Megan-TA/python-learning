from urllib.parse import urlencode
from urllib.request import Request, urlopen

agrs = {
    'wd': 'get请求',
    'ie': 'utf-8'
}

url = 'http://www.baidu.com/s?{}'.format(urlencode(agrs))

print(urlencode(agrs))

print(url)

res = urlopen(Request(url)) 

print(res.read().decode())
