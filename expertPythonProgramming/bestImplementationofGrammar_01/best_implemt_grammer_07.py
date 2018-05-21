#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Tue 15 May 2018 01:45:44 PM CST
# File Name: best_implemt_grammer_07.py
# Description: 一个典型的生成器模板
"""

def my_generator():
    try:
        yield 'something'

    except ValueError:
        yield 'dealing with the exception'

    finally:
        print "ok isn't clean"


gen = my_generator()
print gen.next()
print gen.throw(ValueError('mean mean mean'))   #throw允许客户端代码传入要抛出的任何类型得异常
print gen.close()   #close和throw的工作方式相同，但会抛出名为GeneratorExit的特定异常
#print gen.next()


