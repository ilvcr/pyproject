#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Thu 19 Apr 2018 09:53:02 PM CST
# File Name: match_twosided.py
# Description:  由于数值较高的距离代表两个点能够更好地匹配，所以在排序之前，对距离取相反数。
                    为了获得更稳定的匹配，从第二幅图像向第一幅图像匹配，然后过滤掉在两种方
                        法中不都是最好的匹配
"""

from scipy.ndimage import filters
from pylab import *

def match_twosided(desc1, desc2, threshold=0.5):
    '''两边对称版本的match()'''

    matches_12 = match(desc1, desc2, threshold)
    matches_21 = match(desc2, desc1, threshold)

    ndx_12 = where(matches_12 >= 0)[0]

    #去除非对称的匹配
    for n in ndx_12:
        if matches_21[matches_12[n]\] != n:
            matches_12[n] = -1

    return matches_12

'''
这些匹配可以通过在两边分别绘制出图像，使用线段连接匹配的像素点来直观地可视化
'''
