#!/usr/bin/env python
# -*- coding=utf-8 -*-

'''
 Author       : Yoghourt.Lee->lvcr
 Last modified: 2018-03-25 16:02
 Email        : liyaoliu@foxmail.com or ilvcr@outlook.com
 Filename     : pipelines.py
 Description  :
'''
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.conf import settings
import pymongo

class DoubanspiderPipeline(object):
    def __init__(self):
        #获取setting主机名，端口号和数据库名
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbname = settings['MONGODB_DBNAME']

        #  pymongo.MongoClient(host, port)  创建MongoDB连接
        client = pymongo.MongoClient(host=host, port=port)

        #指向指定的数据库
        mdb = client[dbname]
        #获取数据库里存放的数据的表名
        self.post = mdb[settings['MONGODB_DOCNAME']]


    def process_item(self, item, spider):
        data = dict(item)
        #向指向的表里添加数据
        self.post.insert(data)
        return item
