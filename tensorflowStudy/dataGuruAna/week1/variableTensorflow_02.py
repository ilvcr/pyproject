#!/usr/bin/env python
# -*- coding=utf-8 -*-

'''
 Author       : Yoghourt.Lee->lvcr
 Last modified: 2018-03-18 09:41
 Email        : liyaoliu@foxmail.com or ilvcr@outlook.com
 Filename     : variableTensorflow_02.py
 Description  : 变量 -> tensorflow
'''
import tensorflow as tf

#创建一个变量初始化为0
state = tf.Variable(0, name='counter')
#创建一个op, 作用是是state加1
new_value = tf.add(state, 1)

#赋值op
update = tf.assign(state, new_value)
#变量初始化
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    print(sess.run(state))
    for _ in range(5):
        sess.run(update)
        print(sess.run(state))

