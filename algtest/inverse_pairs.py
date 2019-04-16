#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: inverse_pairs.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 17:56:00 2019
# Description: 寻找对象找的逆序对
#************************************************************************#

from __future__ import print_function

class Solution(object):
    
    def inverse_pairs(self, data):

        count = 0

        for item in sorted(data):
            count += data.index(item)
            data.remove(item)

        return count%1000000007

    def inverse_pairs_000(self, data):

        count = 0

        def merge_sort(lists):

            global count
            if len(lists) <= 1:
                return lists

            num = int(len(lists)/2)
            left = merge_sort(lists[:num])
            right = merge_sort(lists[num:])
            r, l = 0, 0
            result = []

            while l < len(left) and r < len(right):
                if left[l] < right[r]:
                    result.append(left[l])
                    l += 1
                else:
                    result.append(right[r])
                    r += 1
                    count += len(left)-1
                    print 'count: {}'.format(count)

            result += right[r:]
            result += left[l:]

            return result

        merge_sort(data)

        return count%1000000007


