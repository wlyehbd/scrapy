# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from spider.databases.dbfactory.dbfactor import dbfactory
import json


class BlackwindowPipeline(object):
    def close_spider(self, spider):
        print("################################################")
        print("##############close_detail_spider #############")
        print("################################################")


class DetailsPipeline(object):
    def process_item(self, item, spider):
        print("====================DetailsPipeline====================")
        conn = dbfactory.db_redis(conf_name="wlyehbd")
        conn.lpush(spider.config.type, json.dumps(item))
        return item


class SeedsPipeline(BlackwindowPipeline):
    def open_spider(self, spider):
        print("====================SeedsPipeline====================")
        self.conn = dbfactory.db_redis(conf_name="wlyehbd")
        self.config = spider.config

    def process_item(self, item, spider):
        conn = dbfactory.db_redis(conf_name="wlyehbd")
        conn.lpush(spider.config.type, json.dumps(item))
        return item
