#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Mon 09 Apr 2018 02:25:22 PM CST
# File Name: RandomForestAchieveCode.py
# Description:随机森林python实现
"""

#Import Library
from sklearn.ensemble import RandomForestClassifier

#Assumed you have, X (predictor) and Y (target) for training data set and x_test(predictor) of test_dataset
# Create Random Forest object
model= RandomForestClassifier()

# Train the model using the training sets and check score
model.fit(X, y)

#Predict Output
predicted = model.predict(x_test)
