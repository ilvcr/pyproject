#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: testclassfatherandson_03.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Fri Apr  5 22:13:02 2019
# Description: 
#************************************************************************#


class Base:
    def __init__(self):
        print 'Base.__init__'

class A(Base):
    def __init__(self):
        super().__init__()
        print 'A.__init__'

class B(Base):
    def __init__(self):
        super().__init__()
        print 'B.__init__'

class C(A, B):
    def __init__(self):
        super().__init__()
        print 'C.__init__'

c = C()
print c





