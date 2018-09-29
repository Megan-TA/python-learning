from fake_useragent import UserAgent
import requests
import re

url = 'https://www.qiushibaike.com/'

headers = {
    'User-Agent': UserAgent().random
}

# 构造请求
res = requests.get(url, headers= headers)
info = res.text
f1 = re.findall(r'<div class="content">\s*<span>\s*(.+)\s*</span>', info)
with open('qiushibaike.txt', 'w', encoding='utf-8') as f:
    for info in f1:
        f.write(info + '\n\n\n')

# print(s)