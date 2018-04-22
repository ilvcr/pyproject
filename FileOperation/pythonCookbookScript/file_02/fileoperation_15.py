#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 18 Apr 2018 08:34:34 PM CST
# File Name: fileoperation_15.py
# Description:  在不关闭一个已打开的文件的前提下增加或改变其Unicode编码
                代码功能：
                        使用io.TextIOWrapper()的对象给一个二进制模式打开的文件
                        添加Unicode编码/解码方式
"""

import urllib.request
import io

u = urllib.request.urlopen('http://www.python.org')

f = io.TextIOWrapper(u, encoding='utf-8')
text = f.read()
