# -*- coding: utf-8 -*-
import scrapy


class ZwwSpider(scrapy.Spider):
    name = 'zww'
    allowed_domains = ['81zw.us']
    start_urls = [
        'https://www.81zw.us/book/606/424359.html'
    ]

    def parse(self, response):
        title = response.xpath('//h1/text()').extract_first()
        content = ''.join(response.xpath('//div[@id="content"]/text()').extract())

        yield {
            'title': title,
            'content': content
        }

        next_url = response.xpath('//div[@class ="bottem1"]/a[3]/@href').extract_first()
        next_full_url = response.urljoin(next_url)
        yield scrapy.Request(next_full_url, callback=self.parse)
