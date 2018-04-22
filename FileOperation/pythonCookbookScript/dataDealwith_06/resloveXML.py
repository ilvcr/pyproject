#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Thu 19 Apr 2018 08:34:18 PM CST
# File Name: resloveXML.py
# Description:  使用很少的内存增量式的处理一个大型 XML 文件
"""

from xml.etree.ElementTree import iterparse

def parse_and_remove(filename, path):
    path_parts = path.split('/')
    doc = iterparse(filename, ('start', 'end'))

    #skip the root element
    next(doc)

    tag_stack = []
    elem_stack = []
    for event, elem in doc:

        if event == 'start':
            tag_stack.append(elem.tag)
            elem_stack.append(elem)

        elif event == 'end':
            if tag_stack == path_parts:
                yield elem
                elem_stack[-2].remove(elem)
            try:
                tag_stack.pop()
                elem_stack.pop()
            except IndexError:
                pass
