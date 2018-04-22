#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Fri 20 Apr 2018 01:17:55 PM CST
# File Name: write_features_to_file.py
# Description:  将特征位置和描述子保存到文件中
"""

from numpy import savetxt

def write_features_to_file(filename, locs, desc):
    '''将特征位置和描述子保存到文件中 '''

    return savetxt(filename, hstack((locs, desc)))
