#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Thu 03 May 2018 01:29:21 PM CST
# File Name: modules_and_packages_03.py
# Description:  通过钩子远程加载模块
"""

'''
构造如下代码结构:
testcode/
    spam.py
    fib.py
    grok/
        __init__.py
        blah.py
'''

#在每个文件中放入了少量的简单语句和函数，这样你可以测试它们并查看当它们被导入时的输出。

#spam.py
print("I'm spam")

def hello(name):
    print('Hello %s' %name)


#fib.py
print("I'm fib")

def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)



#grok/__init__.py
print("I'm grok.__init__")




#grok/blah.py
print("I'm grok.blah")
