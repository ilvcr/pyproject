#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: merge_sort_linklist.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 14:22:01 2019
# Description:  合并两个排序的链表
#************************************************************************#

class Solution(object):
    '''
        合并两个排序的链表
    '''
    def merge_sort_linklist(self, pHead1, pHead2):

        if pHead1 == None:
            return pHead2
        if pHead2 == None:
            return pHead1

        pMergeHead = None

        if pHead1.val < pHead2.val:
            pMergeHead = pHead1
            pMergeHead.next = self.merge_sort_linklist(pHead1.next, pHead2)
        else:
            pMergeHead = pHead2
            pMergeHead.next = self.merge_sort_linklist(pHead1, pHead2.next)

        return pMergeHead


