#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Tue 15 May 2018 12:01:54 AM CST
# File Name: best_implemt_grammer_04.py
# Description:每个函数用来在序列上定义一个转换，然后他们被连接起来应用，
                    每次调用将处理下一个元素并返回其结果
"""

def power(values):
    for value in values:
        print 'powering {}'.format(value)

        yield value


def adder(values):
    for value in values:
        print 'adding to {}'.format(value)

        if value % 2 == 0:
            yield value + 3
        else:
            yield value + 2


elements = [1, 4, 7, 9, 12, 19, 20]

res = adder(power(elements))

print res.next()
print res.next()
print res.next()
print res.next()
print res.next()
print res.next()






