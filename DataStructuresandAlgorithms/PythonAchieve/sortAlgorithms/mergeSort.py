#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sun 15 Apr 2018 10:52:03 PM CST
# File Name: mergeSort.py
# Description:      归并排序（Merge Sort）
                1->基本思想：
                    归并（Merge）排序法是将两个（或两个以上）有序表合并成一个新的有序表，
                        即把待排序序列分为若干个子序列，每个子序列是有序的。
                        然后再把有序子序列合并为整体有序序列。

                2->合并方法：
                    设r[i…n]由两个有序子表r[i…m]和r[m+1…n]组成，两个子表长度分别为n-i +1、n-m。
                        1)->j=m+1；k=i；i=i; //置两个子表的起始下标及辅助数组的起始下标

                        2)->若i>m 或j>n，转⑷ //其中一个子表已合并完，比较选取结束

                        3)->//选取r[i]和r[j]较小的存入辅助数组rf
                            如果r[i]<r[j]，rf[k]=r[i]； i++； k++； 转(2)
                            否则，rf[k]=r[j]； j++； k++； 转(2)

                        4)->//将尚未处理完的子表中元素存入rf
                            如果i<=m，将r[i…m]存入rf[k…n] //前一子表非空
                            如果j<=n ,  将r[j…n] 存入rf[k…n] //后一子表非空

                        5)->合并结束。
"""

lists=[49,38,65,97,76,13,27,49,55]

#归并排序（Merge Sort）
def merge(left, right):
    i, j = 0, 0
    result = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result

def merge_sort(lists):
    # 归并排序
    if len(lists) <= 1:
        return lists

    num = len(lists) / 2
    left = merge_sort(lists[:num])
    right = merge_sort(lists[num:])

    return merge(left, right)

print(merge_sort(lists))


