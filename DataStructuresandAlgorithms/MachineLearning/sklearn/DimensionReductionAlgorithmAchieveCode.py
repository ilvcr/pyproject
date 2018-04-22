#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Mon 09 Apr 2018 02:27:09 PM CST
# File Name: DimensionReductionAlgorithmAchieveCode.py
# Description:降维算法python实现
"""

#Import Library
from sklearn import decomposition

#Assumed you have training and test data set as train and test
# Create PCA obeject pca= decomposition.PCA(n_components=k) #default value of k =min(n_sample,  n_features)
# For Factor analysis
#fa= decomposition.FactorAnalysis()
# Reduced the dimension of training dataset using PCA
train_reduced = pca.fit_transform(train)

#Reduced the dimension of test dataset
test_reduced = pca.transform(test)

