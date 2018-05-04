#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Fri 04 May 2018 01:30:18 PM CST
# File Name: network_and_web_04.py
# Description:  如何执行一个 HEAD 请求
"""

from http.client import HTTPConnection
from urllib import parse

c = HTTPConnection('www.python.org', 80)
c.request('HEAD', '/index.html')

resp = c.getresponse()

print('Status', resp.status)
for name, value in resp.getheaders():
    print(name, value)
