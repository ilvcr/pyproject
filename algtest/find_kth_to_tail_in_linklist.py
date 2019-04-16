#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: find_kth_to_tail_in_linklist.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 14:05:34 2019
# Description: 链表中倒数第k个节点
#************************************************************************#

class ListNode(object):
    def __init__(slef, x):
        self.val = x
        self.next = None

class Solution(object):
    '''
        链表中倒数第k个节点
    '''
    def find_kth_to_tail_in_linklist(self, head, k):

        if head == None or k <= 0:
            return None

        pAhead = head
        pBhead = None

        for _ in range(k-1):
            if pAhead.next != None:
                pAhead = pAhead.next
            else:
                return None

        pBhead = head
        while pAhead.next != None:
            pAhead = pAhead.next
            pBhead = pBhead.next

        return pBhead


