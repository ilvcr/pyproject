#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: testclassfatherandson_01.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Fri Apr  5 22:03:06 2019
# Description: 
#************************************************************************#


class A:
    def spam(self):
        print 'A.spam'

class B(A):
    def spam(self):
        print 'B.spam'
        super().spam()

class C:
    def __init__(self):
        self.x = 0

class D(C):
    def __init__(self):
        super.__init__()
        self.y = 1







