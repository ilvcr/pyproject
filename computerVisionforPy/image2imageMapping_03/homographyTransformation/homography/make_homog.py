#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sat 21 Apr 2018 07:35:55 PM CST
# File Name: make_homog.py
# Description:  本函数实现对点进行转换其次坐标的功能
"""

from numpy import vstack, ones,
import numpy


def make_homog(points):
    '''将点集（dim×n 的数组）转换为齐次坐标表示'''
    return vstack((points, ones((1, points.shape[1]))))
