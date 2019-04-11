#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: get_number_of_k.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 18:13:54 2019
# Description: 数字再排序数组中出现的次数
#************************************************************************#

class Solution(object):

    def get_number_of_k(self, data, k):

        if not data:
            return 0

        if self.get_last_k(data, k) == -1 and self.get_first_k(data, k) == -1:
            return 0

        return self.get_last_k(data, k) - self.get_first_k(data, k) + 1

    def get_first_k(self, data, k):

        low = 0
        high = len(data) - 1
        while low <= high:
            mid = (low+high) // 2
            if data[mid] < k:
                low = mid + 1
            elif data[mid] > k:
                high = mid - 1
            else:
                if mid == low or data[mid-1] != k:
                    return mid
                else:
                    high = mid - 1

        return -1

    def get_last_k(self, data, k):
        low = 0
        high = len(data) - 1
        while low < high:
            mid = (low+high) // 2
            if data[mid] > k:
                high = mid - 1
            elif data[mid] < k:
                low = mid + 1
            else:
                if mid == high or data[mid+1] != k:
                    return mid
                else:
                    low = mid + 1

        return -1




