from threading import Thread
from queue import Queue
from fake_useragent import UserAgent
import requests
from lxml import etree

url = 'http://www.qiushibaike.com/text/page/{}'

headers = {
    'User-Agent': UserAgent().random
}


# 创建爬虫类
class CrawlInfo(Thread):
    def __init__(self, url_queue, html_queue):
        Thread.__init__(self)
        self.url_queue = url_queue
        self.html_queue = html_queue

    def run(self):
        while not self.url_queue.empty():
            respone = requests.get(self.url_queue.get(), headers=headers)
            if (respone.status_code == 200):
                self.html_queue.put(respone.text)
                print(respone.text)


# 解析类
class ParseInfo(Thread):
    def __init__(self, html_queue):
        Thread.__init__(self)
        self.html_queue = html_queue

    def run(self):
        while not self.html_queue.empty():
            e = etree.HTML(self.html_queue.get())
            span_contents = e.xpath('//div[@class="content"]/span[1]')
            with open('duanzi.txt', 'a', encoding='utf-8') as f:
                for span in span_contents:
                    # 将每一列数据对象序列化
                    info = span.xpath('string(.)')
                    f.write(info + '\n')
                    # print(info)


# 存储url的容器
url_queue = Queue()
# 存储内容的容器
html_queue = Queue()
for i in range(1, 14):
    new_url = url.format(i)
    url_queue.put(new_url)

# 创建一个爬虫
crawl_list = []
for i in range(0, 3):
    crawl1 = CrawlInfo(url_queue, html_queue)
    crawl_list.append(crawl1)
    crawl1.start()

# 依次等待各个线程执行完毕
for crawl in crawl_list:
    # 暂停等待
    crawl.join()

# 最后开始解析数据
parse_list = []
for i in range(0, 3):
    parse = ParseInfo(html_queue)
    parse_list.append(parse)
    parse.start()

for parse in parse_list:
    parse.join()
