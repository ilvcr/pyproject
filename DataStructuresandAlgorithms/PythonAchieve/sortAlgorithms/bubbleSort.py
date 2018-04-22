#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sun 15 Apr 2018 06:21:26 PM CST
# File Name: bubbleSort.py
# Description:
                基本思想：
                    在要排序的一组数中，对当前还未排好序的范围内的全部数，
                    自上而下对相邻的两个数依次进行比较和调整，让较大的数往下沉，较小的往上冒。
                    即：每当两相邻的数比较后发现它们的排序与排序要求相反时，就将它们互换。

"""


lists=[49,38,65,97,76,13,27,49,55]

#交换排序—冒泡排序（Bubble Sort）

def bubble_sort(lists):
    count = len(lists)
    for i in range(count):
        for j in range(i+1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]

    return lists

print(bubble_sort(lists))
