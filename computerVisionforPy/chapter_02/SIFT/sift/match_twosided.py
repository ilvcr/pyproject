#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Fri 20 Apr 2018 01:42:14 PM CST
# File Name: match_twosided.py
# Description:  双向对称版本的 match()
"""

from scipy.ndimage import filters
from pylab import *
from numpy import *


def match_twosided(desc1, desc2):
    '''双向对称版本的 match()'''

    matches_12 = match(desc1, desc2)
    matches_21 = match(desc2, desc1)

    ndx_12 = matches_12.nonzero()[0]

    #去除不匹配的对称
    for n in ndx_12:
        if matches_21[int(matches_12[n])] != n:
            matches_12[n] = 0

    return matches_12
