#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: search_and_two_way_linklist.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 16:49:53 2019
# Description: 二叉搜索树与双向链表
#************************************************************************#

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right right

class Solution(object):
    def convert(self, pRootOfTree):

        if not pRootOfTree:
            return None

        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree

        self.convert(pRootOfTree.left)
        left = pRootOfTree.left

        if left:
            while left.right:
                left = left.right

            pRootOfTree.left = left
            left.right = pRootOfTree

        self.convert(pRootOfTree.right)
        right = pRootOfTree.right

        if right:
            while right.left:
                right = right.left
            pRootOfTree.right = right
            right.left = pRootOfTree

        while pRootOfTree.left:
            pRootOfTree = pRootOfTree.left

        return pRootOfTree



