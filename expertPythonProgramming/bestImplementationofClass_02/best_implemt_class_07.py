#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 16 May 2018 03:14:52 PM CST
# File Name: best_implemt_class_07.py
# Description:  基于内建函数dir的一个非数据描述符可以工作与任何对象类型之上的实例
"""

class API(object):
    def _print_values(self, obj):
        def _print_value(key):
            if key.startswith('_'):
                return ''

            value = getattr(obj, key)
            if not hasattr(value, 'im_func'):
                doc = type(value).__name__
            else:
                if value.__doc__ is None:
                    doc = 'no docstring'
                else:
                    doc = value.__doc__

            return '{}:{}'.format(key, doc)

        res = [_print_value(el) for el in dir(obj)]
        return '\n'.join([el for el in res if el != ''])

    def __get__(self, instance, klass):
        if instance is not None:
            return self._print_values(instance)
        else:
            return self._print_values(klass)


class Myclass(object):
    __doc__ = API()
    def __init__(self):
        self.a = 2

    def meth(self):
        '''my method'''
        return 1


print Myclass.__doc__

instance = Myclass()
print instance.__doc__


