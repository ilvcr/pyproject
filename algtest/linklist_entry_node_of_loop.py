#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: linklist_entry_node_of_loop.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 22:55:04 2019
# Description: 链表中环的入口
#************************************************************************#

class ListNode(object):
    def __init__(slef, x):
        self.val = x
        self.next = None

class Solution(object):

    def linklist_entry_node_of_loop(self, pHead):

        meetNode = self.MeetNode(pHead)
        if not meetNode:
            return None

        loop = 1
        flag = meetNode

        while flag.next != meetNode:
            loop += 1
            flag = flag.next

        fast = pHead
        for _ in range(loop):
            fast = fast.next
        slow = pHead
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast

    def MeetNode(self, head):
        if not head:
            return None
        slow = head.next
        if slow == None:
            return None
        fast = slow.next
        while fast:
            if slow == fast:
                return slow
            slow = slow.next
            fast = fast.next.next




