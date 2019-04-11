#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: search_get_next_node_in_tree.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 23:04:19 2019
# Description: 二叉树的下一个节点
#************************************************************************#

class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution(object):
    def search_get_next_node_in_tree(self, pNode):

        if pNode is None:
            return

        pNext = None

        if pNode.right:
            pNode = pNode.right
            while pNode.left:
                pNode = pNode.left
            pNext = pNode

        else:
            if pNode.next and pNode.next.left == pNode:
                pNext = pNode.next
            elif pNode.next and pNode.next.right == pNode:
                pNode = pNode.next
                while pNode.next and pNode.next.right == pNode:
                    pNode = pNode.next

                if pNode.next:
                    pNext = pNode.next
        return pNext



