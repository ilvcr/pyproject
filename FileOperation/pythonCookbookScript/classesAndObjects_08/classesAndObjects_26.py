#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 25 Apr 2018 07:53:47 PM CST
# File Name: classesAndObjects_26.py
# Description:  利用 Mixins 扩展类功能
                    自定义类的时候会碰上这些问题。可能是某个库提供了一些基础类，可以利用它们来构造自己的类。

                        假设想扩展映射对象，给它们添加日志、唯一性设置、类型检查等等功能。

                                下面是一些混入类：
"""

class LoggedMappingMixin(object):
    '''
    Add logging to get/set/delete operations for debugging
    '''

    __slots__ = () #混入类都没有实例变量, 因为直接实例化混入类没有任何意义

    def __getitem__(self, key):
        print('Getting ' + str(key))
        return super().__getitem__(key)


    def __setitem__(self, key, value):
        print('Setting {} = {!r}'.format(key, value))
        return super().__setitem__(key, value)


    def __delitem__(self, key):
        print('Deleting ' + str(key))
        return super().__delitem__(key)


class SetOnceMappingMixin(object):
    '''
    Only allow a key to be set once
    '''

    __slots__ = ()

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + ' already set')
        return super().__setitem__(key, value)



class StringMappingMixin(object):
    '''
    Restrict keys to strings only
    '''

    __slots__ = ()

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise TypeError('keys must be strings')
        return super().__setitem__(key, value)


#类用来通过多继承来和其他映射对象混入使用
class LoggedDict(LoggedMappingMixin, dict):
    pass

d = LoggedDict()
d['x'] = 23
print(d['x'])
del d['x']

from collections import defaultdict

class SetOnceDefaultDict(SetOnceMappingMixin, defaultdict):
    pass


d = SetOnceDefaultDict(list)
d['x'].append(2)
d['x'].append(3)


