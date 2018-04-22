#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Mon 09 Apr 2018 02:14:06 PM CST
# File Name: NaiveBayesAchieveCode.py
# Description:朴素贝叶斯python实现
"""


#Import Library
from sklearn.naive_bayes import GaussianNB

#Assumed you have, X (predictor) and Y (target) for training data set and x_test(predictor) of test_dataset
# Create SVM classification object 
model = GaussianNB() # there is other distribution for multinomial classes like Bernoulli Naive Bayes, Refer link

#Train the model using the training sets and check score
model.fit(X, y)

#Predict Output
predicted = model.predict(x_test)

