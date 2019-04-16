#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: testclassfatherandson_02.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Fri Apr  5 22:05:11 2019
# Description: 
#************************************************************************#

class Proxy:
    def __init__(slef, obj):
        self._obj = obj

    # Delegate attribute lookup to internal obj
    def __getattr__(self, name):
        return getattr(slef._obj, name)

    # Delegate attribute assignament
    def __setattr__(self, name, value):
        if name.startswith('_'):
            super.__setattr__(name, value)
        else:
            setattr(slef._obj, name, value)


class Base:
    def __init__(self):
        print 'Base.__init__'

class A(Base):
    def __init__(self):
        Base.__init__(self)
        print 'A.__init__'

class B(Base):
    def __init__(self):
        Base.__init__(self)
        print 'B.__init__'

class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print 'C.__init__'

c = C()
print c





