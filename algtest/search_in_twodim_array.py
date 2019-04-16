#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: search_in_twodim_array.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 11:38:35 2019
# Description: 二维数组中的查找
#************************************************************************#

class Solution(object):
    '''
        array  二维数组
    '''
    def find(self, target, array):
        '''
            return True
        '''
        if array == []:
            return False

        num_row = len(array)
        num_col = len(array[0])

        i = num_col - 1
        j = 0

        while i >= 0 and j < num_row:
            if array[j][i] > target:
                i -= 1
            elif array[j][i] < target:
                j += 1
            else:
                return True

if __name__ == '__main__':
    
    result = Solution()
    array = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]]
    print result.find(5, [])



