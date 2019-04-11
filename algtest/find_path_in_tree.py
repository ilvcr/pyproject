#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: find_path_in_tree.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 15:18:02 2019
# Description: 寻找二叉树中和为某一值的路径
#************************************************************************#


class Solution(object):
    
    def find_path_in_tree(self, root, expectNumber):
        '''
            return  二维列表, 内部每个列表表示找到的路径
        '''
        if not root or root.val > expectNumber:
            return []

        if not root.left and not root.right and root.val == expectNumber:
            return [[root.val]]
        else:
            expectNumber -= root.val
            left = self.find_path_in_tree(root.left, expectNumber)
            right = self.find_path_in_tree(root.right, expectNumber)

            result = [[root.val]+i for i in left]
            for i in right:
                result.append([root.val]+i)


        return sorted(result, key=lambda x: -len(x))




