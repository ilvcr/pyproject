#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Mon 09 Apr 2018 01:37:09 PM CST
# File Name: LinearRegressionAchieveCode.py
# Description:机器学习算法线性回归代码实现, python代码
"""

#import Library
#import other necessary libraries like pandas, numpy ...

from sklearn import linear_model

#Load Train and Test datasets
#Identify feature and response variable(s) and values must be numeric and numpy arrays

x_train = input_variables_values_training_datasets
y_train = target_variables_values_training_datasets
x_test = input_variables_values_test_datasets

#Creat linear regression object
linear = linear_model.LinearRegression()

#Train the model using the training sets and check score
linear.fit(x_train, y_train)
linear.score(x_train, y_train)

#Equation coefficient and Intercept
print('Coefficient: n', linear.coef_)
print('Intercept: n', linear.intercept_)

#Predict Output
predicted = linear.predict(x_test)
