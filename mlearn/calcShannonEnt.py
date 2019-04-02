#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: calcShannonEnt.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Tue Apr  2 21:35:12 2019
# Description: 
#************************************************************************#

# 实现熵的计算

def calcShannonEnt(dataSet):
    
    numEntries = len(dataSet)
    
    labelCounts = {}
    
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    
    shannonEnt = 0.0
    
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries
        shannonEnt -= prob * log(prob, 2)
    
    return shannonEnt



