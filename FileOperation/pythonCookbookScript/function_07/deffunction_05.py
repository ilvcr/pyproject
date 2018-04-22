#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Fri 20 Apr 2018 04:35:43 PM CST
# File Name: deffunction_05.py
# Description:  让闭包模拟类的实例。
                    复制上面deffunction_04.py的内部函数到一个字典实例中并返回它即可。
"""

import sys

class ClosureInstance(object):
    def __init__(self, locals=None):
        if locals is None:
            locals = sys._getframe(1).f_locals


        #Update instance dictionary with callables
        self.__dict__.update((key, value) for key, value in locals.items() if callable(value))


    #Redirect special method
    def __len__(self):
        return self.__dict__['__len__']()



#Example use
def Stack():
    items = []
    def push(item):
        items.append(item)

    def pop():
        return items.pop()

    def __len__():
        return len(items)

    return ClosureInstance()
