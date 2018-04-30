#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Mon 30 Apr 2018 01:51:51 AM CST
# File Name: metaprogramming_24.py
# Description:  以编程方式定义类
                    使用函数 types.new class() 来初始化新的类对象。
                    只是提供类的名字、父类元组、关键字参数，以及一个用成员变量填充类字典的回调函数
"""


#stock.py
#Example of making a class manually from parts

#method
def __init__(self, name, shares, price):
    self.name = name
    self.shares = shares
    self.price = price

def cost(self):
    return self.shares * self.price


cls_dict = {
    '__init__' : __init__,
    'cost' : cost,
}

#Make a class
import types

Stock = types.new_class('Stock', (), {}, lambda ns : ns.update(cls_dict))
Stock.__module__ = __name__
