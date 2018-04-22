#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 18 Apr 2018 04:18:38 PM CST
# File Name: transformImageFormat_12.py
# Description:  实现ROF模型进行图像去噪
"""

from numpy import *

def denoise(im, U_init, tolerance=0.1, tau=0.125, tv_weight=100):
    '''
    使用 A. Chambolle 实现 Rudin-Osher-Fatemi（ROF）去噪模型
    输入：含有噪声的输入图像（灰度图像）、 U 的初始值、 TV 正则项权值、步长、停业条件
    输出：去噪和去除纹理后的图像、纹理残留
    '''

    m, n = im.shape #噪声图像大小

    #初始化
    U = U_init
    Px = im  #对偶域的x分量
    Py = im  #对偶域的y分量
    error = 1

    while (error > tolerance):
        Uold = U

        #原始变量的梯度
        GradUx = roll(U, -1, axis=1) - U  #变量U梯度的x分量
        GradUy = roll(U, -1, axis=0) - U  #变量U梯度的y分量
        '''
        roll() 函数在一个坐标轴上，循环“滚动”数组中的元素值。
        该函数可以方便地计算邻域元素的差异，比如导数。
        '''


        #更新对偶变量
        PxNew = Px + (tau / tv_weight) * GradUx
        PyNew = Py + (tau / tv_weight) * GradUy
        NormNew = maximum(1, sqrt(PxNew ** 2 + PyNew ** 2))

        Px = PxNew / NormNew  #更新x分量(对偶)
        Py = PyNew / NormNew  #更新y分量(对偶)

        #更新原始变量
        RxPx = roll(Px, 1, axis=1)  #对x分量进行向右x轴平移
        RyPy = roll(Py, 1, axis=0)  #对y分量进行向右y轴平移

        DivP = (Px - RxPx) + (Py - RyPy)  #对偶域的散度
        U = im + tv_weight * DivP  #更新原始变量

        #更新误差
        error = linalg.norm(U - Uold) / sqrt(n * m)  #linalg.norm()函数，该函数可以衡量两个数组间的差异

    return U, im - U  #去噪后的图像和纹理残余

