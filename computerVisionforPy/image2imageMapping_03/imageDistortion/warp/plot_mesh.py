#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sun 22 Apr 2018 03:41:49 PM CST
# File Name: plot_mesh.py
# Description:  绘制三角形
"""


def plot_mesh(x, y, tri):
    '''绘制三角形'''

    for i in tri:
        t_ext = [t[0], t[1], t[2], t[0]]  #将第一个点加入到最后
        plot(x[t_ext], y[t_ext], 'r')
