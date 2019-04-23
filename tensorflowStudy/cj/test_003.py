#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: test_003.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Fri Apr 19 23:14:55 2019
# Description: 
#************************************************************************#

import tensorflow as tf

#定义参数
x = tf.placeholder(tf.float32, shape=(None, 2))
w1 = tf.Variable(tf.random_normal([2, 3], stddev=1, seed=1))
w2 = tf.Variable(tf.random_normal([3, 1], stddev=1, seed=1))

#fp
a = tf.matmul(x, w1)
y = tf.matmul(a, w2)

#calc
with tf.Session() as sess:
    init_op = tf.global_variables_initializer()
    sess.run(init_op)
    ABC = sess.run(y, feed_dict={x:[[0.7, 0.5], [0.2, 0.3], [0.3, 0.4], [0.4, 0.5]]})
    print 'y in test_003.py is: \n', ABC


