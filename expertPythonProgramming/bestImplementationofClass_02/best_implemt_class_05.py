#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 16 May 2018 03:00:05 PM CST
# File Name: best_implemt_class_05.py
# Description:  不同类的参数
"""

#super用法的另一个问题是初始化中的参数传递

class BaseBase(object):
    def __init__(self, *args, **kwargs):
        print 'basebase'
        super(BaseBase, self).__init__(*args, **kwargs)


class Base1(BaseBase):
    def __init__(self, *args, **kwargs):
        print 'Base1'
        super(Base1, self).__init__(*args, **kwargs)


class Base2(BaseBase):
    def __init__(self, *args, **kwargs):
        print 'Base2'
        super(Base2, self).__init__(*args, **kwargs)


class Myclass(Base1, Base2):
    def __init__(self, arg):
        print 'my base'
        super(Myclass, self).__init__(arg)


print Myclass(10)


