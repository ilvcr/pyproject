#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sun 18 Mar 2018 09:02:23 AM CST
# File Name: createdAndStartGraphs_01.py
# Description:创建图, 启动图  -> tensorflow  ->  方法2
"""

import tensorflow as tf

#创建一个常量op
m1 = tf.constant([[3, 3]])

#创建一个常量op
m2 = tf.constant([[2], [3]])

#创建一个矩阵乘法op, 把m1和m2传入
product = tf.matmul(m1, m2)
print(product)  #观察print(product)的打印结果

with tf.Session() as sess:
    result = sess.run(product)
    print(result)#不需要手动关闭sess

'''
#定义一个会话, 启动默认图
sess = tf.Session()

#调用sess的run方法来执行矩阵乘法op
#run(product)触发了图中的3个op
result = sess.run(product)

print(result)

#这种方法必须关闭sess
sess.close()
'''
#运行结果
'''
Tensor("MatMul:0", shape=(1, 1), dtype=int32)
2018-03-18 09:00:04.390313: I tensorflow/core/platform/cpu_feature_guard.cc:140] Your CPU supports
instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
[[15]]
'''
