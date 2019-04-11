#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: is_continuous_in_card.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 22:03:08 2019
# Description: 扑克牌顺子
#************************************************************************#

class Solution(object):

    def is_continuous_in_card(self, numbers):

        if not numbers or len(numbers) == 0:
            return False

        transdict = {'A':1, 'J':11,'Q':12,'K':13}
        for i in range(len(numbers)):
            if numbers[i] in transdict.keys():
                numbers[i] = transdict[numbers[i]]

        numbers = sorted(numbers)
        number_0 = 0
        number_gap = 0

        i = 0
        while i < len(numbers) and numbers[i] == 0:
            number_0 += 1
            i += 1

        front = number_0
        behind = front + 1
        while behind < len(numbers):
            if numbers[front] == numbers[behind]:
                return False
            number_gap += numbers[behind] - numbers[front] - 1
            front = behind
            behind += 1

        return False if number_gap > number_0 else True



