#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Fri 04 May 2018 01:03:22 PM CST
# File Name: network_and_web_01.py
# Description:  作为客户端与 HTTP 服务交互

                    需要通过 HTTP 协议以客户端的方式访问多种服务。如下载数据或者与基于 REST 的 API 进行交互。
"""

#发送一个简单的 HTTP GET 请求到远程的服务上

from urllib import request, parse

#base URL being accessed
url = 'http://httpbin.org/get'

#Dictionary of query parameters(if any)
parms = {
    'name1' : 'value1',
    'name2' : 'value2'
}

#Encode the query string
querystring = parse.urlencode(parse)

#Make a GET request and read the response
u = request.urlopen(url + '?' + querystring)
resp = u.read()


