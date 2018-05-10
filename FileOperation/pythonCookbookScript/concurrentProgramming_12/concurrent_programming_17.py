#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 09 May 2018 10:21:50 PM CST
# File Name: concurrent_programming_17.py
# Description:  使用 ThreadPoolExecutor 相对于手动实现的一个好处在于它使得任务提交者更方便的从被调用函数中获取返回值
"""

from concurrent.futures import ThreadPoolExecutor
import urllib.request

def fetch_url(url):
    u = urllib.request.urlopen(yrl)
    data = u.read()
    return data


pool = ThreadPoolExecutor(10)
## Submit work to the pool
a = pool.submit(fetch_url, 'http://www.python.org')
b = pool.submit(fetch_url, 'http://www.pypy.org')

#Get the results back
x = a.result()
y = b.result()
