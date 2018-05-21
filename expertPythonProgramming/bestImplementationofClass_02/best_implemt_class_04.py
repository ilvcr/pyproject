#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 16 May 2018 02:54:49 PM CST
# File Name: best_implemt_class_04.py
# Description:  混用super和传统调用
"""

#类C使用__init__方法调用基类,使类B被调用两次

class A(object):
    def __init__(self):
        print 'A'
        super(A, self).__init__()


class B(object):
    def __init__(self):
        print 'B'
        super(B, self).__init__()


class C(A, B):
    def __init__(self):
        print 'C'
        A.__init__(self)
        B.__init__(self)


print "MRO: ", [x.__name__ for x in C.__mro__]

print C()


