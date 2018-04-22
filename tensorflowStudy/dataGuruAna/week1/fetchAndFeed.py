#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sun 18 Mar 2018 11:20:52 AM CST
# File Name: fetchAndFeed.py
# Description:
"""

import tensorflow as tf

#Fetch
#定义三个常量
input1 = tf.constant(3.0)
input2 = tf.constant(4.0)
input3 = tf.constant(5.0)

add = tf.add(input2, input3)
mul = tf.multiply(input1, add)

with tf.Session() as sess:
    result = sess.run([mul, add])
    print(result)


print("\n")

#Feed
#创建占位符
input4 = tf.placeholder(tf.float32)
input5 = tf.placeholder(tf.float32)
output = tf.multiply(input4, input5)

with tf.Session() as sess:
    #feed的数据以字典的形式传入
    print(sess.run(output, feed_dict={input4:[8.], input5:[2.]}))
