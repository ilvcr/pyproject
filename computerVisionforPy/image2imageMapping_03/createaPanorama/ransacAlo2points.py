#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 25 Apr 2018 07:06:42 PM CST
# File Name: ransacAlo2points.py
# Description:  将 RANSAC 算法应用于对应点对上
"""

#将匹配转换成齐次坐标点的函数
def convert_points(j):
    ndx = matches[j].nonzero()[0]
    fp = homography.make_homog(l[j+1][ndx,:2].T)
    ndx2 = [int(matches[j][i]) fpr i in ndx]
    tp = homography.make_homog(l[j][ndx2,:2].T)

    return fp, tp


#估计单应性矩阵
model = homography.RansacModel()

fp, tp = convert_points(1)
H_12 = homography.H_from_ransac(fp, tp, model)[0]  #im1 到 im2 的单应性矩阵


fp, tp = convert_points(0)
H_01 = homography.H_from_ransac(fp, tp, model)[0]  #im0 到 im1 的单应性矩阵


tp,fp = convert_points(2) # 注意：点是反序的
H_32 = homography.H_from_ransac(fp, tp, model)[0]  #im3 到 im2 的单应性矩阵


tp,fp = convert_points(3) # 注意：点是反序的
H_43 = homography.H_from_ransac(fp,tp,model)[0] # im4 到 im3 的单应性矩阵


'''
在该例中，图像 2 是中心图像，也是我们希望将其他图像变成的图像。图像 0 和图像 1 应该从右边扭曲，
图像 3 和图像 4 从左边扭曲。在每个图像对中，由于匹配是从最右边的图像计算出来的，
所以我们将对应的顺序进行了颠倒，使其从左边图像开始扭曲。因为我们不关心该扭曲例子中的正确点对，
所以仅需要该函数的第一个输出（单应性矩阵）
'''

