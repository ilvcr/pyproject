#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sun 29 Apr 2018 12:04:11 AM CST
# File Name: metaprogramming_17.py
# Description:  用一个简单的类，使用这个排序字典来实现将一个类实例的数据序列化为一行CSV 数据
"""


class Structure(metaclass=OrdereMeta):
    def as_csv(self):
        return ','.join(str(getattr(self, name)) for name in self._order)



#Example use
class Stock(Structure):
    name = String()
    shares = Integer()
    price = Float()


    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price



s = Stock('GOOG', 100, 490.1)
print(s.name)

