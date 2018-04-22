#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sun 18 Mar 2018 11:36:45 AM CST
# File Name: simpleDemoTensorflow.py
# Description:
"""
import tensorflow as tf
import numpy as np

#使用numpy生成2000个随机点
x_data = np.random.rand(2000)
y_data = x_data * 0.1 + 0.2

#构造一个线性模型
b = tf.Variable(0.)
k = tf.Variable(0.)
y = k * x_data + b

#二次代价函数
loss = tf.reduce_mean(tf.square(y_data - y)) #reduce_mean方法为求平均值
#定义一个梯度下降法来进行训练的优化器
optimizer = tf.train.GradientDescentOptimizer(0.2)
#最小化代价函数
train = optimizer.minimize(loss)

#初始化变量
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for step in range(20001):
        sess.run(train)
        if step % 40 == 0:
            print(step, sess.run([k, b]))
