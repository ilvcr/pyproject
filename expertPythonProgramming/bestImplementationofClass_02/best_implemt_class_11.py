#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Thu 17 May 2018 12:00:44 AM CST
# File Name: best_implemt_class_11.py
# Description:  两个具体的行为必须被应用到一个类，可以使用一个“增强函数”来添加
"""

def enhancer_1(klass):
    c = [l for l in klass.__name__ if l.isupper()]
    klass.contracted_name = ''.join(c)


def enhancer_2(klass):
    def logger(function):
        def wrap(*args, **kwargs):
            print 'I log everything!'
            return function(*args, **kwargs)
        return wrap

    for el in dir(klass):
        if el.startswith('-'):
            continue

        value = getattr(klass, el)

        if not hasattr(value, 'im_func'):
            continue

        setattr(klass, el, logger(value))

def enhancer(klass, *enhancers):
    for enhancer in enhancers:
        enhancer(klass)


class MySimpleClass(object):
    def ok(self):
        '''I return ok'''
        return 'I lied'

enhancer(MySimpleClass, enhancer_1, enhancer_2)
thats = MySimpleClass()

print thats.ok()

#print thats.score

print thats.contracted_name


