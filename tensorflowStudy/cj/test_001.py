#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: test_001.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Fri Apr 19 22:51:14 2019
# Description: 
#************************************************************************#

import tensorflow as tf
a = tf.constant([1.0, 2.0])
b = tf.constant([3.0, 4.0])
result  = a + b
print result

print '======================='

x = tf.constant([[1.0, 2.0]])
w = tf.constant([[3.0], [4.0]])
y = tf.matmul(x, w)
print y

print '======================='
with tf.Session() as sess:
    print sess.run(y)


