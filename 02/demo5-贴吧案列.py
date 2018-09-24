from urllib.request import Request, urlopen
from urllib.parse import urlencode
from fake_useragent import UserAgent

def get_html(url):
    headers = {
        'User-Agent': UserAgent().chrome
    }
    request = Request(url, headers = headers)
    res = urlopen(request)
    print(res.read().decode())
    return res.read()

def save_html(fileName, html_bytes):
    with open(fileName, 'wb') as f:
        f.write(html_bytes)

def main():
    kw = input('请输入要查询的关键词：')
    num = input('请输入要下载的页数：')
    base_url = 'http://tieba.baidu.com/f?ie=utf=8&{}'

    for pn in range(int(num)):
        args = {
            'kw': kw,
            'pn': pn * 50
        }
        args = urlencode(args)
        file_name = '第' + str(pn + 1) + '页.html'
        print('正在下载', file_name)
        full_url = base_url.format(args)
        print(full_url)
        html_bytes = get_html(full_url)
        save_html(file_name, html_bytes)
        
main()