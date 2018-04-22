#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Mon 09 Apr 2018 02:19:41 PM CST
# File Name: KMeansAchieveCode.py
# Description:K-均值算法python实现
"""

#Import Library
from sklearn.cluster import KMeans

#Assumed you have, X (attributes) for training data set and x_test(attributes) of test_dataset
# Create KNeighbors classifier object model
#k_means = Kmeans(n_clusters=3, random_state=0)
model = Kmeans(n_clusters=3, random_state=0)

#Train the model using the training sets and check score
model.fit(X)

#predict Output
predicted = model.predoct(x_test)
