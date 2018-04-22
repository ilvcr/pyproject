#!/usr/bin/env python
# -*- coding=utf-8 -*-

'''
 Author       : Yoghourt.Lee->lvcr
 Last modified: 2018-04-08 14:09
 Email        : liyaoliu@foxmail.com or ilvcr@outlook.com
 Filename     : KNNAchieveCode.py
 Description  : 最邻近代码
'''

import numpy as np

class NearestNeighbor:
    def __init__(self):
        pass

    #记录所有训练数据
    def train(self, X, y):
        """X is N x D where each row is an example. Y is 1-dimension of size N"""
        #the nearest neighbor classifier simple remember all the training data
        self.Xtr = X
        self.ytr = y

    def predict(self, X):
        """X is N x D where each row is an example we wish to predict label for"""
        num_test = X.shape[0]
        #lets make sure that the output type matches the input type
        Ypred = np.zeros(num_test, dtype = self.ytr.dtype)

        #loop over all teat rows
        for i in xrange(num_test):
            #find the nearest training image to the i'th test image
            #using the L1 distance (sum of absolute value differences)
            distances = np.sum(np.abs(self.Xtr - X[i,:]), axis = 1)
            min_index = np.argmin(distances)#get the index with smallest distance
            Ypred[i] = self.ytr[min_index]#predict the label of the nearest example

        return Ypred


"""
#import for sklearn

#Import Library
from sklearn.neighbors import KNeighborsClassifier

#Assumed you have, X (predictor) and Y (target) for training data set and x_test(predictor) of test_dataset
# Create KNeighbors classifier object 
model =  KNeighborsClassifier(n_neighbors=6) # default value for n_neighbors is 5


# Train the model using the training sets and check score
model.fit(X, y)

#Predict Output
predicted= model.predict(x_test)
"""
