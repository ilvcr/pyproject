# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


#class MobileappcapturereptilesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #pass

class MobileAppCaptureReptilesspiderItem(scrapy.Item):
    name = scrapy.Field()#存储照片的名字
    imageUrls = scrapy.Field()#照片的url途径
    imagePath = scrapy.Field()#照片保存在本地的路径
