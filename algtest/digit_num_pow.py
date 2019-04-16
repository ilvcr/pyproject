#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: digit_num_pow.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Apr 11 13:54:47 2019
# Description: 整数的整数次方
#************************************************************************#

class Solution(object):
    '''
        整数的整数次方
    '''
    def power(self, base, exponent):

        try:
            ret = self.power_value(base, abs(exponent))
            if exponent < 0:
                return 1.0 / ret
        except ZeroDivisionError:
            print 'Error: base is zero'
        else:
            return ret

    def power_value(self, base, exponent):

        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        ret = self.power_value(base, exponent >> 1)
        ret *= ret

        if exponent & 1 == 1:
            ret *= base

        return ret


