#!/usr/bin/env python
# -*- coding=utf-8 -*-

import scrapy
import json
from MobileAppCaptureReptiles.items import MobileAppCaptureReptilesspiderItem

class MobileAppCaptureReptilesSpider(scrapy.Spider):
    name = "MobileAppCaptureReptiles"
    allowd_domains = ["http://cpi.douyucdn.cn"]

    offset = 0
    url = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset="
    start_urls = [url + str(offset)]

    def parse(self, response):
        #返回json里获取 data段数据集合

        data = json.loads(response.text)["data"]

        for each in data:
            item = MobileAppCaptureReptilesspiderItem()
            item["name"] = each["nikename"]
            item["imageUrls"] = each["vertical_src"]

            yield item


        self.offset += 20
        yield scrapy.Request(self.url + str(self.offset), callback = self.parse)
