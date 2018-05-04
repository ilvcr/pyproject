#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Fri 04 May 2018 01:12:56 PM CST
# File Name: network_and_web_02.py
# Description:  需要在发出的请求中提供一些自定义的 HTTP 头，如修改 user-agent字段,
                    可以创建一个包含字段值的字典，并创建一个 Request 实例然后将其传给urlopen() 
"""

from urllib import request, parse


#Extra headers
headers = {
    'User-agent' : 'none/ofyourbunsiness',
    'Spam' : 'Eggs'
}


req = request.Request(url, querystring.encoding('ascii'), headers=headers)

#Make a request and read the response
u = request.urlopen(req)
resp = u.read()



#采用 requests 库重新实现了上面的操作  network_and_web_01.02

import requests

#Base URL being accessed
url = 'http://httpbin.org/post'

# Dictionary of query parameters (if any)
parms = {
    'name1' : 'value1',
    'name2' : 'value2'
}


#Extra headers
headers = {
    'User-agent' : 'none/ofyourbusiness',
    'Spam' : 'Eggs'
}

resp = requests.post(url, data=parms, headers=headers)


#Decoded text returned by the request
text = resp.text
