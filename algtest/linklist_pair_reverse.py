#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: linklist_pair_reverse.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Fri Apr 12 10:55:08 2019
# Description: 1->2->3->4 转换成 2->1->4->3
#************************************************************************#

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    '''
        @param a ListNode
        @return a ListNode
    '''
    def swap_pairs(self, head):
        if head != None and head.next != None:
            next = head.next
            head.next = self.swap_pairs(next.next)
            next.next = head
            return next
        return head

if __name__ == '__main__':
    pass



