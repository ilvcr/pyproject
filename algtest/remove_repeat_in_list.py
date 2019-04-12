#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: remove_repeat_in_list.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Fri Apr 12 10:46:50 2019
# Description: 
#************************************************************************#

l = [1, 1, 2, 15, 3, 4, 4, 3, 5, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print l
print '===================\n'

#使用set
print list(set(l))
print '===================\n'

#使用字典
print {}.fromkeys(l)
print '===================\n'
print {}.fromkeys(l).keys()

print '===================\n'
l1 = [1, 1, 2, 15, 3, 4, 4, 3, 5, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
l2 = []
print [l2.append(i) for i in l1 if not i in l2]






