#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: yang_matrix_do.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Fri Apr 12 10:30:13 2019
# Description: 杨氏矩阵查找
#************************************************************************#

'''
    在一个m行n列二维数组中，每一行从左到右、从上到下都为递增序列，
    请完成一个函数，输入一个二维数组和整数，判断数组中是否含有h该整数
'''

class yangMatDo(object):

    def __init__(self):
        pass

    def get_value(self, l, r, c):
        return l[r][c]

    def find(self, l, x):
        m = len(l) - 1
        n = len(l[0]) - 1
        r = 0
        c = n
        while c >= 0 and r <= m:
            value = self.get_value(l, r, c)
            if value == x:
                return True and [[r],[c]]
            elif value > x:
                c -= 1
            else:
                r += 1
        return True

if __name__ ==  '__main__':
    ym = yangMatDo()
    l = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]] 
    print ym.get_value(l, 1, 3) 
    print '=======================\n'
    gb = ym.find(l, 4)
    print gb
    print '=======================\n'


