#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: knapsack.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: 2018年07月24日 星期二 21时28分57秒
# Description: 
'''
    Given weights and values of n items, put these items in a knapsack of 
    capacity W to get the maximum total value in the knapsack.
'''
#************************************************************************#


def knapsack(W, wt, val, n):
    dp = [[0 for i in range(W+1)] for j in range(n+1)]

    for i in range(1, n+1):
        for w in range(1, W+1):
            if(wt[i-1] <= w):
                dp[i][w] = max(val[i-1] + dp[i-1][w-wt[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][w]



