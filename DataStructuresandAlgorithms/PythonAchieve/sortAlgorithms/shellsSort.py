#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sun 15 Apr 2018 02:22:10 PM CST
# File Name: shellsSort.py
# Description:          插入排序—希尔排序（Shell`s Sort）

                1->希尔排序又叫缩小增量排序
                2->基本思想：先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，
                待整个序列中的记录“基本有序”时，再对全体记录进行依次直接插入排序。
                3->操作方法：
                    1)->选择一个增量序列t1，t2，…，tk，其中ti>tj，tk=1；
                    2)->按增量序列个数k，对序列进行k 趟排序；
                    3)->每趟排序，根据对应的增量ti，将待排序列分割成若干长度为m
                        的子序列，分别对各子表进行直接插入排序。仅增量因子为1
                        时，整个序列作为一个表来处理，表长度即为整个序列的长度。
                4->算法实现：
                    简单处理增量序列：增量序列d = {n/2 ,n/4, n/8 .....1}n为要排序数的个数。
                    即：先将要排序的一组记录按某个增量d（n/2,n为要排序数的个数）分成若干组子序列，
                    每组中记录的下标相差d.对每组中全部元素进行直接插入排序，
                    然后再用一个较小的增量（d/2）对它进行分组，在每组中再进行直接插入排序。
                    继续不断缩小增量直至为1，最后使用直接插入排序完成排序。
"""

lists=[49,38,65,97,76,13,27,49,55]

#插入排序—————希尔排序（Shell`s Sort）
def shell_sort(lists):
    count = len(lists)
    step = 2
    group = count / step

    while group > 0:
        for i in range(group):
            j = i + group

            while j < count:
                key = lists[j]
                k = j - group

                while k >= 0:
                    if lists[k] > key:
                        lists[k+group] = lists[k]
                        lists[k] = key
                    k = k - group
                j = j + group
        group = group / step
    return lists

print(shell_sort(lists))


'''
希尔排序时效分析很难，关键码的比较次数与记录移动次数依赖于增量因子序列d的选取，
特定情况下可以准确估算出关键码的比较次数和记录的移动次数。
增量因子序列可以有各种取法，有取奇数的，也有取质数的，但需要注意：增量因子中除1外没有公因子，
且最后一个增量因子必须为1。
希尔排序方法是一个不稳定的排序方法。
'''
