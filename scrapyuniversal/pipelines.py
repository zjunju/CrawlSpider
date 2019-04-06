# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import json


class ScrapyuniversalPipeline(object):
    def open_spider(self, spider):
        path = os.path.join("data", spider.file_name+'.json')
        self.fo = open(path, 'a', encoding='utf-8')

    def process_item(self, item, spider):
        json_data = dict(item)
        self.fo.write(json.dumps(json_data, ensure_ascii=False))
        self.fo.write("\n")
        return item

    def close_spider(self, spider):
        self.fo.close()
