#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: is_symetrical_in_tree.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 23:08:55 2019
# Description: 对称的二叉树
#************************************************************************#

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def is_symetrical_in_tree(slef, pRoot):
        return self.self_is_sym(pRoot, pRoot)

    def self_is_sym(self, root1, root2):
        if root1 == root2 and root2 == None:
            return True
        if root1 == None or root2 == None:
            return Fasle
        if root1.val != root2.val:
            return False

        return self.self_is_sym(root1.left, root2.right)
               and self.self_is_sym(root1.right, root2.left)



