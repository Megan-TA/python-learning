# -*- coding: utf-8 -*-
import scrapy

class ZolSpider(scrapy.Spider):
    name = 'zol'
    allowed_domains = ['desk.zol.com.cn']
    start_urls = [
        'http://desk.zol.com.cn/bizhi/7239_89590_2.html'
    ]


    def parse(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()

        image_urls = response.xpath('//img[@id="bigImg"]/@src').extract()
        image_name = response.xpath('string(//h3)').extract_first()

        yield {
            'image_urls': image_urls,
            'image_name': image_name
        }

        next_urls = response.xpath('//a[@id="pageNext"]/@href').extract_first()
        if next_urls.find('.html') != -1:
            yield scrapy.Request(response.urljoin(next_urls), callback=self.parse)
