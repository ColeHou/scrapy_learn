# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient

class QiubaiPipeline(object):

    def __init__(self,mongo_port,mongo_db):
        self.mongo_port  = mongo_port
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            mongo_port = crawler.settings.get('MONGO_PORT'),
            mongo_db = crawler.settings.get('MONGO_DB')

        )   
    def open_spider(self,spider):
        self.Client = MongoClient(self.mongo_port)
        self.db = self.Client[self.mongo_db]

    def close_spider(self,spider): 
        self.Client.close()  

    def process_item(self, item, spider):
        collection_name = item.__class__.__name__
        self.db[collection_name].insert(dict(item))
        return item
