#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: merge_two_sort_linklist.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Fri Apr 12 11:06:10 2019
# Description: 合并两个有序列表
#************************************************************************#


class Solution(object):

    def merge_two_sort_linklist1(self, l1, l2, tmp):
        if len(l1) == 0 or len(l2) == 0:
            tmp.extend(l1)
            tmp.extend(l2)
        else:
            if l1[0] < l2[0]:
                tmp.append(l1[0])
                del l1[0]
            else:
                temp.append(l2[0])
                del l2[0]
            return merge_two_sort_linklist1(l1, l2 ,temp)

    def merge_two_sort_linklist2(self, l1, l2):
        return self.merge_two_sort_linklist1(l1, l2, [])
                
    
    def loop_merge_sort(self, l1, l2):
        tmp = []
        while len(l1) > 0 and len(l2) > 0:
            if l1[0] < l2[0]:
                tmp.append(l1[0])
                del l1[0]
            else:
                tmp.append(l2[0])
                del l2[0]

        tmp.extend(l1)
        tmp.extend(l2)
        return tmp

    def merge_sortedlist(self, a, b):
        c = []
        while a and b:
            if a[0] >= b[0]:
                c.append(b.pop(0))
            else:
                c.append(a.pop(0))
        while a:
            c.append(a.pop(0))
        while b:
            c.append(b.pop(0))
        return c



