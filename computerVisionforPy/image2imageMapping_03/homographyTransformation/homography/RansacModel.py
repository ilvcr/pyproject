#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 25 Apr 2018 06:45:09 PM CST
# File Name: RansacModel.py
# Description:  用于测试单应性矩阵的类，
其中单应性矩阵是由网站 http://www.scipy.org/Cookbook/RANSAC上的 ransac.py 计算出来的
"""

class RansacModel(ogject):
    '''
    用于测试单应性矩阵的类，其中单应性矩阵是由网站 http://www.scipy.org/Cookbook/RANSAC 上
    的 ransac.py 计算出来
    '''


    def __init__(self, debug=False):
        self.debug = debug


    def fit(self, data):
        ''' 计算选取的 4 个对应的单应性矩阵'''

        #将其转置，来调用 H_from_points() 计算单应性矩阵
        data = data.T

        # 映射的起点
        fp = data[:3, :4]

        #映射的目标点
        tp = data[3:, :4]

        #计算单应性矩阵, r然后返回
        return H_from_points(fp, tp)


    def get_error(self, data, H):
        '''对所有的对应计算单应性矩阵，然后对每个变换后的点，返回相应的误差 '''

        data = data.T

        # 映射的起始点
        fp = data[:3]

        # 映射的目标点
        tp = data[3:]

        #变换fp
        fp_transformed = dot(H, fp)

        #归一化齐次坐标
        for i in range(3):
            fp_transformed[i] /= fp_transformed[2]

        #返回每个点的误差
        return sqrt(sum((tp-fp_transformed)**2, axis=0))
