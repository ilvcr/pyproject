#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: test_002.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Fri Apr 19 23:01:51 2019
# Description: 
#************************************************************************#

import tensorflow as tf

#生成随机数的函数
#tf.random_normal()     #生成正态分布随机数
#tf.truncated_normal()  #生成去掉过大偏离点的正态分布随机数
#tf.random_uniform()    #生成均匀分布随机数
#tf.zeros               #表示生成全0数组
#tf.ones                #表示生成全1数组
#tf.fill                #表示c生成全定值数组
#tf.constant            #表示生成直接给定值的数组

w = tf.Variable(tf.random_normal([2, 3], stddev=2, mean=0, seed=1))
'''
生成正态分布随机数，形状两行三列，标准差为2，均值为0，随机种子为1
'''

w = tf.Variable(tf.truncated_normal([2, 3], stddev=2, mean=00, seed=1))
'''
表示去掉偏离过大的正态分布，
如果随机出来的数据偏离平均值超过2个标准差，此数据将重新生成
'''

w = tf.random_uniform(shape=7, minval=0, maxval=1, dtype=tf.int32, seed=1)
'''
表示从一个均匀分布[minval, maxval)中随机采样
'''




