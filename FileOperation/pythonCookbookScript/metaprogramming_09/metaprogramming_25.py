#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Mon 30 Apr 2018 01:57:54 AM CST
# File Name: metaprogramming_25.py
# Description:  使用一个” 框架魔法”，通过调用 sys._getframe()来获取调用者的模块名。
"""


import operator
import types
import sys

def name_tuple(classname, fieldnames):
    #Populate a dictiionary of field property accessors
    cls_dict = {name: property(operator.itemgetter(n)) for n, name in enumerate(fieldnames)}


    #Make a __new__ function and add to the class dict
    def __new__(cls, *args):
        if len(args) != len(fieldnames):
            raise TypeError('Expected {} argument'.format(len(fieldnames)))
            return tuple.__new__(cls, args)


    cls_dict['__new__'] = __new__


    #Make the class
    cls = types.new_class(classname, (tuple,), {}, lambda ns: ns.update(cls_dict))


    #Set the module to that of the caller
    cls.__module__ = sys._getframe(1).f_global['__name__']

    return cls
