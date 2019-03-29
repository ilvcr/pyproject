#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: testlist_01.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Fri Mar 29 12:33:10 2019
# Description: 
#************************************************************************#


numbers = range(10)
print numbers

print '------------------------------'

size = len(numbers)

evens = []

i = 0

while i < size:
    if i % 2  == 0:
        evens.append(i)
    i += 1

print evens

print '----------------------------------'


list1 = [i for i in range(10) if i % 2 == 0]
print list1


