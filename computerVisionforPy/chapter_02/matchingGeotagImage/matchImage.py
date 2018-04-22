#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Fri 20 Apr 2018 02:11:38 PM CST
# File Name: matchImage.py
# Description:  假设已经对这些图像使用 SIFT 特征提取代码进行了处理，
                    并且将特征保存在和图像同名（但文件名后缀是 .sift，而不是 .jpg）的文件中。
                假设 imlist 和 featlist 列表中包含这些文件名, 对所有组合图像对进行逐个匹配
"""

import sift

nbr_images = len(imlist)

matchscores = zeros((nbr_images, nbr_images))
for i in range(nbr_images):
    for j in range(i, nbr_images):#仅仅计算三角形
        print("comparing", imlist[i], imlist[j])


        l1 ,d1 = sift.read_features_from_file(featlist[i])
        l2, d2 = sift.read_features_from_file(featlist[j])

        matches = sift.match_twosided(d1, d2)

        nbr_matches = sum(matches > 0)
        print("number of matches = ", nbr_matches)
        matchscores[i, j] = nbr_matches

        #复制值
        for i in range(nbr_images):
            for j in range(i+1, nbr_images):  #不需要复制对角线
                matchscores[j, i] = matchscores[i, j]
