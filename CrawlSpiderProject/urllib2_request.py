#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: urllib2_request.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Fri Apr 26 15:04:38 2019
# Description: 
#************************************************************************#

import urllib2

request = urllib2.Request('http://www.baidu.com')

response = urllib2.urlopen(request)

html = response.read()

print html


