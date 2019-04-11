#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: tree_depth_solution.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 18:20:48 2019
# Description: 二叉树的深度
#************************************************************************#

class TreeNode(object):
    self.val = x
    self.left = None
    self.right = None

class Solution(object):

    def tree_depth_solution(self, pRoot):

        if not pRoot:
            return 0

        return max(self.TreeNode(pRoot.left), self.TreeNode(pRoot.right)) + 1



