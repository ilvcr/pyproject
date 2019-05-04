#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: use_urlopen.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Fri Apr 26 15:03:00 2019
# Description: 
#************************************************************************#

import urllib2

response = urllib2.urlopen('http://www.baidu.com')

html = response.read()

print html

