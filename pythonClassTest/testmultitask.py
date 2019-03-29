#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: testmultitask.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Fri Mar 29 13:04:42 2019
# Description: 
#************************************************************************#


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

print '-------------------------------------'
print multitask.add(coroutine_1())

print '-------------------------------------'

print multitask.add(coroutine_2())
print '-------------------------------------'
print multitask.run()
print '-------------------------------------'








