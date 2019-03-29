#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: testfunc_01.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Fri Mar 29 12:52:26 2019
# Description: 
#************************************************************************#



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

elements = [1, 4 ,7, 9, 12, 19, 27]

res = adder(power(elements))
print '--------------------------'
print res.next()
print '--------------------------'
print res.next()
print '--------------------------'
print res.next()
print '--------------------------'
print res.next()
print '--------------------------'
print res.next()
print '--------------------------'
print res.next()
