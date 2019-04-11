#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: min_number_in_rotate_array.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 13:03:31 2019
# Description: 旋转数组的最小数字
#************************************************************************#


class Solution(object):
    '''
        旋转数组的最小数字
    '''
    def min_number_in_rotate_array(self, rotateArray):

        if len(rotateArray) == 0:
            
            return 0

        front = 0
        rear = len(rotateArray) - 1
        minVal = rotateArray[0]

        if rotateArray[front] < rotateArray[rear]:
            
            return rotateArray[front]
        else:

            while (rear - front) > 1:
                mid = (front + rear) // 2

                if rotateArray[mid] >= rotateArray[front]:
                    
                    front = mid
                elif rotateArray[mid] <= rotateArray[rear]:

                    rear = mid
                elif rotateArray[front] == rotateArray[rear] == rotateArray[mid]:

                    for i in range(1, len(rotateArray)):                
                        if rotateArray[i] < minVal:

                            minVal = rotateArray[i]
                            rear = i
            minVal = rotateArray[rear]
            return minVal



