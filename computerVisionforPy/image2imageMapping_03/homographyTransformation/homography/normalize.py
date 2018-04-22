#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sat 21 Apr 2018 07:31:20 PM CST
# File Name: normalize.py
# Description:  本函数实现对点进行归一化的功能
"""

def normalize(point):
    '''在一次坐标意义下, 对点集进行归一化, 使最后一行为 1'''
    for row in points:
        row /= points[-1]
    return points
