#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: verify_squence_of_BST.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 15:13:49 2019
# Description: 二叉搜索树的后序遍历序列
#************************************************************************#

class Solution(object):

    def verify_squence_of_BST(self, sequence):

        if sequence == []:
            return False

        length = len(sequence)
        root = sequence[-1]

        for i in range(length):
            if sequence[i] > root:
                break

        for j in range(i, length):
            if sequence[j] < root:
                return False

        left = True
        if i > 0:
            left = self.verify_squence_of_BST(sequence[:i])
        right = True
        if j < length - 1:
            right = self.verify_squence_of_BST(sequence[i:length-1])

        return left and right





