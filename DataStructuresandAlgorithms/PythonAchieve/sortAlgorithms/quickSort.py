#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sun 15 Apr 2018 10:37:54 PM CST
# File Name: quickSort.py
# Description:      交换排序—快速排序（Quick Sort）
                基本思想：
                    1)->选择一个基准元素,通常选择第一个元素或者最后一个元素,
                    2)->通过一趟排序讲待排序的记录分割成独立的两部分，其中一部分记录的元素值均比基准元素值小。
                        另一部分记录的元素值比基准值大。
                    3)->此时基准元素在其排好序后的正确位置
                    4)->然后分别对这两部分记录用同样的方法继续进行排序，直到整个序列有序。

                时间复杂度:
                    O(nlog2n)
"""

lists=[49,38,65,97,76,13,27,49,55] 

right = len(lists)
#交换排序—快速排序（Quick Sort）

def quick_sort(lists, left, right):
    #快速排序
    if left >= right:
        return lists

    key = lists[left]
    low = left
    high = right

    while left< right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]

        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]

    lists[right] = key
    quick_sort(lists, low, left - 1)
    quick_sort(lists, left + 1, high)
    return lists

print(quick_sort(lists, 0, right - 1))
