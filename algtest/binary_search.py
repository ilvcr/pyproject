#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: binary_search.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Fri Apr 12 11:17:04 2019
# Description: 二分查找
#************************************************************************#

def binary_search(lists, item):

    low = 0
    high = len(lists) - 1
    while low <= high:
        guss = (low+high) / 2
        #guss = list[mid]
        if guss > item:
            high = guss - 1
        elif guss < item:
            low = guss + 1
        else:
            return guss
    return None

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9]
print binary_search(mylist, 19)



