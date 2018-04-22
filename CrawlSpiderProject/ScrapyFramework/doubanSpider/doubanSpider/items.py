#!/usr/bin/env python
# -*- coding=utf-8 -*-
'''
 Author       : Yoghourt.Lee->lvcr
 Last modified: 2018-03-25 15:47
 Email        : liyaoliu@foxmail.com or ilvcr@outlook.com
 Filename     : items.py
 Description  :
'''

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #pass
    #电影标题
    title = scrapy.Field()
    #电影评分
    score = scrapy.Field()
    #电影信息
    content = scrapy.Field()
    #简介
    info = scrapy.Field()
