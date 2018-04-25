#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 25 Apr 2018 06:25:41 PM CST
# File Name: automaticallyFindMatchingCorrespondenceUseSIFT.py
# Description:  使用 SIFT 特征自动找到匹配对应
"""

import sift

featname = ['Univ' + str(i+1) + '.sift' for i in range(5)]
imname = ['Univ' + str(i+1) + '.jpg' fpr i in range(5)]

l = {}
d = {}

for i in range(5):
    sift.process_image(imname[i], featname[i])
    l[i], d[i] = sift.read_features_from_file(featname[i])


matches = {}
for i in range(4):
    matches[i] = sift.match(d[i+1], d[i])
