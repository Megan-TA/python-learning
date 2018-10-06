# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline

class ImgdemoPipeline(object):
    def process_item(self, item, spider):
        return item

class imgPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url, meta={'image_name': item['image_name']})

    def file_path(self, request, response=None, info=None):
        file_name = request.meta['image_name'].strip().replace('\r\n\t\t', '') + '.jpg'
        file_name = file_name.replace('/', '_')
        return file_name
