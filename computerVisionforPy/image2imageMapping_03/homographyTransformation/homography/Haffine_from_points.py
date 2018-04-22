#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sat 21 Apr 2018 08:23:25 PM CST
# File Name: Haffine_from_points.py
# Description:  使用对应点对来计算仿射变换矩阵
"""

def Haffine_from_points(fp, tp):
    '''计算 H，仿射变换，使得 tp 是 fp 经过仿射变换 H 得到的'''

    if fp.shape != tp.shape:
        raise RuntimeError('number of points do not match')

    #对点进行归一化
    #---映射起始点---
    m = mean(fp[:2], axis=1)
    maxstd = max(std(fp[:2], axis=1)) + 1e-9
    C1 = diag([1/maxstd, 1/maxstd, 1])
    C1[0][2] = -m[0] / maxstd
    C1[1][2] = -m[1] / maxstd
    fp_cond = dpt(C1, fp)


    #---映射对应点---
    m =mean(tp[:2], axis=1)
    C2 = C1.copy() #两个点集, 必须都进行相同的缩放
    C2[0][2] = -m[0] / maxstd
    C2[1][2] = -m[1] / maxstd
    C2[1][2] = dot(C2, tp)
    tp_cond = dot(C2, tp)

    #因为归一化后点的均值为0, 所以平移量为0
    A = concatenate((fp_cond[:2], tp_cond), axis=0)
    U, S, V = linalg.svd(A.T)

    #如Hartley和Zisserman所著Multiple View Geometry in Computer, Scond Edition 所示,
    #创建矩阵B和C
    tmp = V[:2].T
    B = tmp[:2]
    C = tmp[2:4]

    tmp2 = concatenate((dot(C, linalg.pinv(B)), zeros((2, 1))), axis=1)
    H = vstack((tmp2, [0, 0, 1]))

    #反归一化
    H = dot(linalg.inv(C2), dot(H, C1))

    return H / H[2, 2]
