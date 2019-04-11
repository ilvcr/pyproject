#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: balance_tree_solution.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 18:23:17 2019
# Description: 平衡二叉树
#************************************************************************#

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def __init__(self):
        self.flag = True

    def balance_tree_solution(self, pRoot):

        self.get_depth(pRoot)
        return self.flag

    def get_depth(self, root):

        if not root:
            return 0

        left = self.get_depth(root.left) + 1
        right = self.get_depth(root.right) + 1

        if abs(left-right) > 1:
            self.flag = False

        return left if left > right else right




