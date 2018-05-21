#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 16 May 2018 02:37:44 PM CST
# File Name: best_implemt_class_02.py
# Description:  list类型是用一个序列来管理类型内部工作室会使用到的序列
"""

class folder(list):
    def __init__(self, name):
        self.name = name

    def dir(self):
        print 'I am the {} folder.'.format(self.name)
        for element in self:
            print element


the = folder('secret')

print the

the.append('pics')
the.append('videos')

print the.dir()


