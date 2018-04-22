#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Mon 09 Apr 2018 02:29:23 PM CST
# File Name: BoostingAchieveCode.py
# Description:boosting 算法的Gradient Boosting 和 AdaBoost  的python实现
"""

#Import Library
from sklearn.ensemble import GradientBoostingClassifier

#Assumed you have, X (predictor) and Y (target) for training data set and x_test(predictor) of test_dataset
# Create Gradient Boosting Classifier object
model= GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=0)

# Train the model using the training sets and check score
model.fit(X, y)

#Predict Output
predicted = model.predict(x_test)
