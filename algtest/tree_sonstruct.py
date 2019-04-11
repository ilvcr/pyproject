#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: tree_sonstruct.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 14:29:43 2019
# Description: 树的子结构
#************************************************************************#

class TreeNode(object):
    def __init__(slef, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    '''
        树的子结构
    '''
    def has_subtree(self, pRoot1, pRoot2):

        result = False
        if pRoot1 != None and pRoot2 != None:
            if pRoot1.val == pRoot2.val:
                result = self.does_tree1_have_tree2(pRoot1, pRoot2)
            if not result:
                result = self.has_subtree(pRoot1.left, pRoot2)
            if not result:
                result = self.has_subtree(pRoot1.right, pRoot2)

    def does_tree1_have_tree2(self, pRoot1, pRoot2):

        if pRoot2 == None:
            return True
        if pRoot1 == None:
            return False
        if pRoot1.val != pRoot2.val:
            return False

        return self.does_tree1_have_tree2(pRoot1.left, pRoot2.left) \
               and self.does_tree1_have_tree2(pRoot1.right, pRoot2.right)



