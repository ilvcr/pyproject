#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Fri 20 Apr 2018 01:14:35 PM CST
# File Name: read_features_from_file.py
# Description:  读取特征属性值，然后将其以矩阵的形式返回
"""

from numpy import loadtxt

def read_features_from_file(filename):
    '''读取特征属性值，然后将其以矩阵的形式返回'''

    f = loadtxt(filename)
    return f[:,:4],f[:,4:]#特征位置, 描述子
