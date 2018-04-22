#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sun 15 Apr 2018 02:12:00 PM CST
# File Name: straightInsertionSort.py
# Description:插入排序, 直接插入排序(Straight Insertion Sort)----稳定排序

                效率：
                时间复杂度：O（n^2）
"""

lists = [49,38,65,97,76,13,27,49,55]

#插入排序—————直接插入排序(Straight Insertion Sort)
def insert_sort(lists):
    count = len(lists)
    for i in range(1, count):
        j = i - 1
        key = lists[i]
        while j >= 0:
            if key < lists[j]:
                lists[j+1] = lists[j]
                lists[j] = key
                #print lists
            j = j - 1
    return lists


#print("-------------------------------------")
print(insert_sort(lists))


'''
插入算法把要排序的数组分成两部分：第一部分包含了这个数组的所有元素，
但将最后一个元素除外（让数组多一个空间才有插入的位置），
而第二部分就只包含这一个元素（即待插入元素）。
在第一部分排序完成后，再将这个最后元素插入到已排好序的第一部分中i。
'''
