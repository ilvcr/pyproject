#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Mon 09 Apr 2018 01:48:35 PM CST
# File Name: LogisticRegressionAchieveCode.py
# Description:逻辑回归python实现, 分类算法
"""

#import Library
from sklearn.linear_model import LogisticRegression
#Assumed you have,X(predictor) and Y(target) for training data set and x_test(predictor) of test_dataset
#Create Logistic Regression object

model = LogisticRegression()

#Train the model using the training sets and check score
model.fit(X, y)
model.score(X, y)

#Equation coefficient and Intercept
print('Coefficient: n', model.coef_)
print('Intercept: n', model.intercept_)

#Predict Output
predicted = model.predict(x_test)

