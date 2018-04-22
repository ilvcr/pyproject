#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Mon 16 Apr 2018 06:11:48 PM CST
# File Name: deffunction_03.py
# Description:  代码功能: 允许使用者根据某个模板方案来获取到URL链接地址
"""

from urllib.request import urlopen

class UrlTemplate(object):
    def __init__(self, template):
        self.template = template

    def open(self, **kwargs):
        return urlopen(self.template.format_map(kwargs))

#Example use. Download stock data from yahoo
yahoo = UrlTemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
for line in yahoo.open(names='IBM,AAPL,FB', fields='sl1c1v'):
    print(line.decode('utf-8'))

'''
#代替代码(函数方法)
def urltemplate(template):
    def opener(**kwargs):
        return urlopen(template.format_map(kwargs))  #闭包
    return opener

#Example use
yahoo = urltemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
for line in yahoo(names='IBM,AAPL,FB', fields='sl1c1v'):
    print(line.decode('utf-8'))
'''

