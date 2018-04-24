#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Mon 23 Apr 2018 11:27:20 PM CST
# File Name: classesAndObjects_14.py
# Description:  简化数据结构的初始化
                    不在 fields 中的名称加入到属性中去
"""


class Structure3(object):
    #Class variable that specifies expected fields
    _fields = []


    def __init__(self, *args, **kwargs):
        if len(args) != len(self._fields):
            raise TypeError('Expect {} argument'.format(len(self._fields)))


        #Set the arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)


        #Set the additional arguments(if any)
        extra_args = kwargs.keys() - self._fields
        for name in extra_args:
            setattr(self, name, kwargs.pop(name))


        if kwargs:
            raise TypeError('Duplicate value for {}'.format(','.join(kwargs)))


#Example use
if __name__ == "__main__":
    class Stock(Structure3):
        _fields = ['name', 'shares', 'price']


    s1 = Stock('ACME', 50, 91.1)
    s2 = Stock('ACME', 50, 91.1, date='24/4/2018')
