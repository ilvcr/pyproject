#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Tue 15 May 2018 01:51:50 PM CST
# File Name: best_implemt_grammer_08.py
# Description:  使用multitask模块实现Trampoline模式，看作是生产和消费数据的协同程序之间的媒介
"""

import multitask
import time

def coroutine_1():
    for i in range(3):
        print 'c1'
        yield i


def coroutine_2():
    for i in range(3):
        print 'c2'
        yield i


multitask.add(coroutine_1())
multitask.add(coroutine_2())

print multitask.run()


