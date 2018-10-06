# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class DemoPipeline(object):
    def open_spider(self, spider):
        self.file_name = open('xiaoshuo.txt', 'w', encoding='utf-8')
    def process_item(self, item, spider):
        # 保存数据到文本
        # dict 序列化
        self.file_name.write(json.dumps(dict(item), ensure_ascii=False) + '\n')
        return item
    def close_spider(self, spider):
        self.file_name.close()
