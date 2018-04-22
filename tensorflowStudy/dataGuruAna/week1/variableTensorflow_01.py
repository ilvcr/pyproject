#!/usr/bin/env python
# -*- coding=utf-8 -*-

'''
 Author       : Yoghourt.Lee->lvcr
 Last modified: 2018-03-18 09:31
 Email        : liyaoliu@foxmail.com or ilvcr@outlook.com
 Filename     : variableTensorflow_01.py
 Description  : 变量 -> tensorflow
'''

import tensorflow as tf

#设置一个变量
x = tf.Variable([1, 2])
#设置一个常量
a = tf.constant([3, 3])

#增加一个减法op
sub = tf.subtract(x, a)

#增加一个加法op
add = tf.add(x, sub)

init = tf.global_variables_initializer() #变量初始化

with tf.Session() as sess:
    sess.run(init) #运行初始化变量
    print(sess.run(sub))
    print(sess.run(add))

