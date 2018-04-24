#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Mon 23 Apr 2018 08:05:53 PM CST
# File Name: classesAndObjects_11.py
# Description:  定义一个延迟属性的一种高效方法是通过使用一个描述器类
                    解决计算出的值被创建后可以被修改的缺陷
                        实现不太高效

                缺点是所有 get 操作都必须被定向到属性的 getter 函数上去。
                    这个跟之前简单的在实例字典中查找值的方案相比效率要低一点。
"""


def lazyproperty(func):
    name = '_lazy_' + func.__name__

    @property
    def lazy(self):
        if hasattr(self, name):
            return getattr(self, name)

        else:
            value = func(self)
            setattr(self, name, value)
            return value

    return lazy
