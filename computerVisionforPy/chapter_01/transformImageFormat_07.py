#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Mon 16 Apr 2018 11:54:09 PM CST
# File Name: transformImageFormat_07.py
# Description:  图像的主成分分析(PCA)-->>非常有用的降维技巧
                代码功能：
                        该函数首先通过减去每一维的均值将数据中心化，然后计算协方差矩阵对应最大特征值的特征向量，
                        此时可以使用简明的技巧或者 SVD 分解。这里我们使用了range() 函数，
                        该函数的输入参数为一个整数 n，函数返回整数 0...(n-1) 的一个列表。
                        也可以使用arange()函数来返回一个数组，或者使用xrange()函数返回一个产生器（可能会提升速度）。
"""

from PIL import Image
from numpy import *

def pca(X):
    '''
    主成分分析：
    输入：矩阵 X，其中该矩阵中存储训练数据，每一行为一条训练数据
    返回：投影矩阵（按照维度的重要性排序）、方差和均值
    '''

    #获取维数
    num_data, dim = X, shape

    #数据中心化
    mean_X = X.mean(axis=0)
    X = X - mean_X

    if dim > num_data:
        #PCA-使用紧致技巧
        M = dot(X, X.T) #协方差矩阵
        e, EV = linalg.eigh(M) #特征值和特征向量
        tmp = dot(X.T, EV).T #紧致技巧
        V = tmp[::-1] #由于最后的特征向量为所需, 需将其逆转
        S = sqrt(e)[::-1] #由于特征值是按照递增顺序排列的，需将其逆转

        for i in range(V.shape[1]):
            V[:, i] /= S

    else:
    # PCA -使用SVD方法
    U, S, V = linalg.svd(X)
    V =V[num_data:] #返回前num_data维的数据为合理

    #返回投影矩阵, 方差和均值
    return V, S, mean_X

'''
PCA（Principal Component Analysis，主成分分析） 产生的投影矩阵可以被视为将原始坐标变换到现有的坐标系，
坐标系中的各个坐标按照重要性递减排列。为了对图像数据进行 PCA 变换，图像需要转换成一维向量表示。
可以使用NumPy 类库中的 flatten() 方法进行变换。将变平的图像堆积起来，我们可以得到一个矩阵，
矩阵的一行表示一幅图像。在计算主方向之前，所有的行图像按照平均图像进行中心化。

通常使用 SVD（SingularValue Decomposition，奇异值分解）方法来计算主成分；但当矩阵的维数很大时，
SVD 的计算非常慢，所以此时通常不使用 SVD 分解。
'''
