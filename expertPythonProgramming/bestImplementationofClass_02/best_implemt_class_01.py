#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 16 May 2018 02:24:23 PM CST
# File Name: best_implemt_class_01.py
# Description:  展示的新式类不允许存在多个相同的键值
"""

class DistinctError(Exception):
    pass


class distinctdict(dict):
    def __setitem__(self, key, value):
        try:
            value_index = self.values().index(value)
            '''
            #只要dict在两次调用之间没有发生改变
            #keys()和values()将返回相应的列表
            #否则，dict类型无法保证序列的顺序
            '''
            existing_key = self.keys()[value_index]
            if existing_key != key:
                raise DistinctError(("This value already  \
                                     exists for '%s'")%str(self[existing_key]))

        except ValueError:
            pass


        super(distinctdict, self).__setitem__(key, value)


my = distinctdict()
my['key'] = 'value'
my['other_key'] = 'value'

print my


