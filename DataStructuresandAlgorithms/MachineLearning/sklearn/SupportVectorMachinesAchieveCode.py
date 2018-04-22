#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Mon 09 Apr 2018 02:05:28 PM CST
# File Name: SupportVectorMachinesAchieveCode.py
# Description:支持向量机python实现
"""

#Import Library
from sklearn import svm

#Assumed you have,X (predictor) and Y (target) for training data set and x_test(predictor) of test_dataset
model = svm.svc()
#there is various option associated with it, this is simple for classification. You can refer link, for mo# re detail.

#Train the model using the training sets and check score
model.fit(X, y)
model.score(X, y)

#Predict Output
predicted = model.predict(x_test)
