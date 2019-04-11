#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: clockwise_print_matrix.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 14:41:32 2019
# Description: 顺时针打印矩阵
#************************************************************************#

class Solution(object):
    '''
        matrix类型为二维矩阵, 需要返回列表
    '''
    def print_matrix(self, matrix):

        if not matrix:
            return []

        rows = len(matrix)
        columns = len(matrix[0])
        start = 0
        result = []

        while rows > start * 2 and columns > start * 2:
            self.clockwise_print_matrix(matrix, columns, rows, start, result)
            start += 1

        return result

    def clockwise_print_matrix(self, matrix, columns, rows, start, result):

        endX = columns - 1 - start
        endY = rows - 1 - start

        #从左到右打印一行
        for i in range(start, endX+1):
            result.append(matrix[start][i])

        #从上到下打印一行
        if start < endY:
            for i in range(start+1, endY+1):
                result.append(matrix[i][endX])

        #从右到左打印一行
        if start < endX and start < endY:
            for i in range(endX-1, start-1, -1):
                result.append(matrix[endY][i])

        #从下到上打印一行
        if start < endX and start < endY-1:
            for i in range(endY-1, start, -1):
                result.append(matrix[i][start])



