#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Tue 24 Apr 2018 12:01:47 AM CST
# File Name: classesAndObjects_16.py
# Description:  实现数据模型的类型约束
                    定义某些在属性赋值上面有限制的数据结构
                        使用描述器自定义属性赋值函数, 使用描述器实现了一个系统类型和赋值验证框架
"""

#Base class.Uses a descriptor to set a value
class Descriptor(object):
    def __init__(self, name=None, **opts):
        self,name = name
        for key, value in opts.items():
            setattr(self, key, value)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value



#Descriptor for enforcing types
class Type(Descriptor):
    expected_type = type(None)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('expected ' + str(self.expected_type))
        super().__set__(instance, value)


#Descriptor for enforcing values
class Usinged(Descriptor):
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Expected >= 0')
        super().__set__(instance, value)


class MaxSized(Descriptor):
    def __init__(self, name=None, **opts):
        if 'size' not in opts:
            raise TypeError('missing size option')
        super().__init__(name, **opts)

    def __set__(self, instance, value):
        if len(value) >= self.size:
            raise ValueError('Size must be < ' + str(self.size))
        super().__set__(instance, value)

