#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Thu 19 Apr 2018 09:43:51 PM CST
# File Name: match.py
# Description:  与harris.py中一起使用
"""

from scipy.ndimage import filters
from pylab import *

def match(desc1, desc2, threshold=0.5):
    '''对于第一幅图像中的每个角点描述子，使用归一化互相关，选取它在第二幅图像中的匹配角点'''

    n = len(desc1[0])

    #点对的距离
    d = -ones((len(desc1), len(desc2)))
    for i in range(len(desc1)):
        for j in range(len(desc2)):
            d1 = (desc1[i] - mean(desc1[i])) / std(desc1[i])
            d2 = (desc2[j] - mean(desc2[j])) / std(desc2[j])
            ncc_value = sum(d1 * d2) / (n - 1)
            if ncc_value > threshold:
                d[i, j] = ncc_value

    ndx = argsort(-d)
    matchscores = ndx[:, 0]

    return matchscores
