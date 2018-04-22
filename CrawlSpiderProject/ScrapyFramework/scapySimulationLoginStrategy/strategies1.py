#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Tue 03 Apr 2018 02:10:11 PM CST
# File Name: strategies1.py
# Description:策略一：直接POST数据（比如需要登陆的账户信息)
"""

import scrapy

class RenrenSpider(scrapy.Spider):
    name = 'renren1'
    allowed_domains = ["renren.com"]


    def start_requests(self):
        url = 'http://www.renren.com/Plogin.do'
        #FormRequest 是 Scrapy发送的POST请求的方法
        yield scrapy.FormRequest(
                    url = url,
                    formdata = {"email" : "mr_mao_hacker@163.com", "password" : "axxxxxxxe"},
                    callback = self.parse_page)

        def parse_page(self, response):
            with open("mao2.html", "w") as filename:
                filename.write(response.body)

