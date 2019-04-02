#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: skRandomForest.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Tue Apr  2 22:00:26 2019
# Description: 
#************************************************************************#


from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=1000)

model.fit(X, y)

predicted = model.predict(x_test)


