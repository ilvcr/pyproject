#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sat 21 Apr 2018 07:46:09 PM CST
# File Name: H_from_points.py
# Description:  使用线性 DLT 方法，计算单应性矩阵 H，使 fp 映射到 tp。点自动进行归一化
"""

from numpy import *

def H_from_points(fp, tp):
    '''使用线性 DLT 方法，计算单应性矩阵 H，使 fp 映射到 tp。点自动进行归一化'''

    if fp.shape != tp.shape:
        raise RuntimeError('number of points do not match')

    #对点进行归一化(对数值计算很重要)
    #---映射起始点---

    m = mean(fp[:2], axis=1)
    maxstd = max(std(fp[:2], axis=1)) + 1e-9
    C1 = diag([1/maxstd, 1/maxstd, 1])
    C1[0][2] = -m[0] / maxstd
    C1[1][2] = -m[1] / maxstd
    fp = dot(C1, fp)

    #---映射对应点---
    m = mean(tp[:2], axis=1)
    maxstd = max(std(tp[:2], axis=1)) + 1e-9

    C2 = diag([1/maxstd, 1/maxstd, 1])
    C2[0][2] = -m[0] / maxstd
    C2[1][2] = -m[1] / maxstd
    tp = dot(C2, tp)

    #创建用于线性方法的矩阵, 对于每个对应对, 在矩阵中会出现两行数值
    nbr_correspondences = fp.shape[1]
    A = zeros((2 * nbr_correspondences, 9))
    for i in range(nbr_correspondences):
        A[2*i] = [-fp[0][i], -fp[1][i], -1, 0, 0, 0, tp[0][i]*fp[0][i],tp[0][i]*fp[1][i],tp[0][i]]
        A[2*i+1] = [0 ,0 ,0 ,-fp[0][i] ,-fp[1][i] ,-1 ,tp[1][i]*fp[0][i] ,tp[1][i]*fp[1][i] ,tp[1][i]]

    U, S, V = linalg.svd(A)
    H = V[8].reshape((3, 3))

    #反归一化
    H= dot(linalg.inv(C2), dot(H, C1))

    #归一化, 然后返回
    return H / H[2, 2]


'''
函数H_from_points的第一步操作是检查点对的两个数组中点的数目是否相同。
如果不相同，函数将会抛出异常信息
'''
