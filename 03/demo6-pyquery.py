from pyquery import PyQuery as pq
import requests
from fake_useragent import UserAgent

url = 'http://www.xicidaili.com/nn'

headers = {
    'User-Agent': UserAgent().chrome
}

response = requests.get(url, headers = headers)
doc = pq(response.text)
ips = doc('#ip_list tr').eq(1).find('td').eq(1).text()
trs = doc('#ip_list tr')
for num in range(1, len(trs)):
    ip = trs.eq(num).find('td').eq(1).text()
    print('ip:' + ip)

print(ips)