#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: quick_sort.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Fri Apr 12 11:22:47 2019
# Description: 快排
#************************************************************************#

def quick_sort(lists):
    if len(lists)<2:
        return lists
    else:
        midpivot = lists[0]
        lessbeformidpivot = [i for i in lists[1:] if i <= midpivot]
        biggerafterpivot = [i for i in lists[1:] if i > midpivot]
        finallylist = quick_sort(lessbeformidpivot) + [midpivot] + quick_sort(biggerafterpivot)
        return finallylist

a = [1, 2 , 453, 15, 22, 6, 4, 43, 536, 5, 42, 87]
print quick_sort(a)




