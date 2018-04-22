#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Fri 20 Apr 2018 01:32:03 PM CST
# File Name: match.py
# Description:  对于第一幅图像中的每个描述子，选取其在第二幅图像中的匹配
                    输入： desc1（第一幅图像中的描述子）， desc2（第二幅图像中的描述子）
"""
from scipy.ndimage import filters
from pylab import *
from numpy import *

def match(desc1, desc2):
    '''
    对于第一幅图像中的每个描述子，选取其在第二幅图像中的匹配
    输入： desc1（第一幅图像中的描述子）， desc2（第二幅图像中的描述子）
    '''

    desc1 = array([d/linalg.norm(d) for d in desc1)
    desc2 = array([d/linalg.norm(d) for d in desc2)

    dise_ratio = 0.6
    desc1_size = desc1.shape

    matchscores = zeros((desc1_size[0], 1), 'int')
    desc2t = desc2.T  #预先计算矩阵转置
    for i in range(desc1_size[0]):
        dotprods = dot(desc1[i,:],desc2t)  #向量点乘
        dotprods = 0.9999 * dotprods
        #反余弦和反排列, 返回第二幅图像中特征的索引
        index = argsort(arccos(dotprods))

        #检查最邻近的角度是否小于dise_ratio乘以第二邻近的角度
        if arccos(dotprods)[indx[0]] < dise_ratio * arccos(dotprods)[indx[1]]:
            matchscores[i] = int(indx[0])

        return matchscores
