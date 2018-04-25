#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 25 Apr 2018 06:57:21 PM CST
# File Name: H_from_ransac.py
# Description:  使用 RANSAC 稳健性估计点对应间的单应性矩阵 H

                # 输入：齐次坐标表示的点 fp， tp（3×n 的数组）
"""

def H_from_ransac(fp, tp, model, maxiter=1000, match_theshold=10):
    '''使用 RANSAC 稳健性估计点对应间的单应性矩阵 H
            （ransac.py 为从http://www.scipy.org/Cookbook/RANSAC 下载的版本）
        # 输入：齐次坐标表示的点 fp， tp（3×n 的数组）
    '''
    import ransac

    #对应点组
    data = vstack((fp, tp))

    #计算H, 并返回
    H, ransac_data = ransac.ransac(data.T, model, 4, maxiter, match_theshold, 10, return_all=True)

    return H, ransac_data['inliers']

