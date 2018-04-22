#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sun 15 Apr 2018 02:42:40 PM CST
# File Name: simpleSelectionSort.py
# Description:      选择排序—简单选择排序（Simple Selection Sort）
                1->基本思想：
                        在要排序的一组数中，选出最小（或者最大）的一个数与第1个位置的数交换；
                        然后在剩下的数当中再找最小（或者最大）的与第2个位置的数交换，
                        依次类推，直到第n-1个元素（倒数第二个数）和第n个元素（最后一个数）比较为止。

                2->操作方法：
                        第一趟，从n 个记录中找出关键码最小的记录与第一个记录交换；
                        第二趟，从第二个记录开始的n-1 个记录中再选出关键码最小的记录与第二个记录交换；
                        以此类推.....
                        第i 趟，则从第i 个记录开始的n-i+1 个记录中选出关键码最小的记录与第i 个记录交换，
                        直到整个序列按关键码有序。
"""

lists=[49,38,65,97,76,13,27,49,55]

#选择排序—————简单选择排序（Simple Selection Sort）

def select_sort(lists):
    count = len(lists)
    for i in range(count):
        min = i
        for j in range(i+1, count):
            if lists[min] > lists[j]:
                min = j
        lists[min], lists[i] = lists[i], lists[min]
    return lists

print(select_sort(lists))
