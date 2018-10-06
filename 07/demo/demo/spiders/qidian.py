# -*- coding: utf-8 -*-
import scrapy
from demo.items import DemoItem


class QidianSpider(scrapy.Spider):
    name = 'qidian'
    allowed_domains = ['qidian.com']
    start_urls = [
        'https://www.qidian.com/rank/yuepiao'
    ]
    # 加入需要导出json、xml、csv格式的数据
    # scrapy crawl qidian -o book.json
    def parse(self, response):
        # extract 选择出一组数据
        names = response.xpath('//h4/a/text()').extract()
        authors = response.xpath('//p[@class="author"]/a[1]/text()').extract()
        # print(names, authors)
        book = []
        item = DemoItem()
        for name, author in zip(names, authors):
            book.append({
                "name": name,
                "author": author
            })
            # 给item部分赋值
            item["name"] = name
            item["author"] = author
            # yield部分代码走pipelines管道任务
            yield item

        # print(book)
        return book
