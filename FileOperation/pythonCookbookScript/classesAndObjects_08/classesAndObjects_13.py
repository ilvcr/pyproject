#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Mon 23 Apr 2018 11:17:24 PM CST
# File Name: classesAndObjects_13.py
# Description:  支持关键字参数，可以将关键字参数设置为实例属性
                        简化数据结构的初始化
"""

class Structure2:
    _fields = []


    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError('Expected {} arguement'.format(len(self._fields)))


        #Set all of the positional arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)


        #Set the remaining keyword arguments
        for name in self._fields[lem(args)]:
            setattr(self, name, kwargs.pop(name))


        #Check for any remaining unknown argument
        if kwargs:
            raise TypeError('Invalid argument(s):{}'.format(','.join(kwargs)))


#Example use
if __name__ == '__mian__':
    class Stock(Structure2):
        _fields = ['name', 'shares', 'price']


    s1 = Stock('ACME', 50, 91.1)
    s2 = Stock('ACME', 50, price=91.1)
    s3 = Stock('ACME', shares=50, price=91.1)
