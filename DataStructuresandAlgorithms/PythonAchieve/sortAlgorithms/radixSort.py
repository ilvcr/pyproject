#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sun 15 Apr 2018 11:02:23 PM CST
# File Name: radixSort.py
# Description:      桶排序/基数排序(Radix Sort)
                基数排序:
                    是按照低位先排序，然后收集；再按照高位排序，然后再收集；
                        依次类推，直到最高位。有时候有些属性是有优先级顺序的，
                        先按低优先级排序，再按高优先级排序。
                        最后的次序就是高优先级高的在前，高优先级相同的低优先级高的在前。
                        基数排序基于分别排序，分别收集，所以是稳定的。
"""

import math

lists=[49,38,65,97,76,13,27,49,55]

#桶排序/基数排序(Radix Sort)

def radix_sort(lists, radix=10):
    k = int(math.ceil(math.log(max(lists), radix)))
    bucket = [[] for i in range(radix)]

    for i in range(1, k+1):
        for j in lists:
            bucket[j / (radix ** (i - 1)) % (radix ** i)].append(j)

        del lists[:]
        for z in bucket:
            lists += z
            del z[:]

    return lists

print(radix_sort(lists))
