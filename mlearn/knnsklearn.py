#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: knnsklearn.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Tue Apr  2 21:21:13 2019
# Description: 
#************************************************************************#

import numpy as np
from sklearn import neighbors

# knn分类器
knn = neighbors.KNeighborsClassifier()

data = np.array([[3, 104], [2, 100], [1, 81], [101, 10], [99, 5], [98, 2]])

labels = np.array([1, 1, 1, 2, 2, 2])

knn.fit(data, labels)

knn.predict([18, 90])


