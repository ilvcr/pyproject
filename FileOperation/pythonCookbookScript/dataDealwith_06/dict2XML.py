#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Thu 19 Apr 2018 08:42:55 PM CST
# File Name: dict2XML.py
# Description:  使用一个 Python 字典存储数据，并将它转换成 XML 格式
"""

from xml.etree.ElementTree import Element

def dict_to_xml(tag, d):
'''
Turn a simple dict of key/value into XML
'''

elem = Element(tag)
for key, val in d.items():
    child = Element(key)
    child.text = str(val)
    elem.append(child)
return elem
