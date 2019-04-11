#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: delete_duplication_in_linklist.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 23:00:13 2019
# Description: 删除链表中的重复节点
#************************************************************************#

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def delete_duplication_in_linklist(self, pHead):

        if pHead is None or pHead.next is None:
            return pHead

        first = ListNode(-1)
        first.next = pHead
        last = first

        while pHead and pHead.next:
            if pHead.val == pHead.next.val:
                val = pHead.val
                while pHead and val == pHead.val:
                    pHead = pHead.next
                last.next = pHead
            else:
                last = pHead
                pHead = pHead.next

        return first.next

