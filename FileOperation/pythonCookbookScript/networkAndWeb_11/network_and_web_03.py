#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Fri 04 May 2018 01:17:16 PM CST
# File Name: network_and_web_03.py
# Description:  用 requests 库发起一个 HEAD 请求，并从响应中提取出一些HTTP 头数据的字段
"""

import requests

resp = requests.head('http://www.python.org/index.html')

status = resp.status_code
last_modified = resp.headers['last-modified']
content_type = resp.headers['content-type']
content_length = resp.headers['content-length']


'''
Here is a requests example that executes a login into the Python Package index using
basic authentication:
'''
import requests

resp = requests.get('http://pypi.python.org/pypi?:action=login', auth=('user','password'))

'''
Here is an example of using requests to pass HTTP cookies from one request to the next
'''

import requests

#First request
resp1 = requests.get(url)


# Second requests with cookies received on first requests
resp2 = requests.get(url, cookies=resp1.cookies)


'''
Last, but not least, here is an example of using requests to upload content:
'''

import requests

url = 'http://httpbin.org/post'
files = {'file':('data.csv', open('data.csv', 'rb'))}


r = requests.post(url, files=files)
