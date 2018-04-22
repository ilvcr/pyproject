#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : 2018年03月23日 星期五 13时22分08秒
# File Name: seeImageTensorflow.py
# Description: tensorflow可视化
"""

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
from tensorflow.contrib.tensorboard.plugins import projector

#载入数据集
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
#运行次数
max_step = 1001
#图片数量
image_num = 3000
#文件路径
DTR = '/home/ilvcr/pythonStudy/tensorflowStudy/week4/TensorflowforSeeImages'

#定义会话
sess = tf.Session()
#载入图片
embedding = tf.Variable(tf.stack(mnist.test.images[:image_num]), trainable=False,name='embedding')
#参数概要
def variable_summaries(var):
    with tf.name_scope("summaries"):
        mean = tf.reduce_mean(var)
        tf.summary.scalar("mean", mean)#平均值
        with tf.name_scope("stddev"):
            stddev = tf.sqrt(tf.reduce_mean(tf.square(var - mean)))
        tf.summary.scalar("stddev", stddev)#标准差
        tf.summary.scalar("max", tf.reduce_max(var))#最大值
        tf.summary.scalar("min", tf.reduce_min(var))#最小值
        tf.summary.histogram("histogram", var)#直方图


#命名空间
with tf.name_scope("input"):
    #定义两个placeholder
    x = tf.placeholder(tf.float32, [None, 784], name='x-input')
    y = tf.placeholder(tf.float32, [None, 10], name='y-input')


with tf.name_scope("layer"):
    #创建一个简单的神经网络
    with tf.name_scope("wights"):
        W = tf.Variable(tf.zeros([784, 10]), name="W")
        variable_summaries(W)
    with tf.name_scope("biases"):
        b = tf.Variable(tf.zeros([10]),name="b")
        variable_summaries(b)
    with tf.name_scope("wx_plus_b"):
        wx_plus_b = tf.matmul(x, W) + b
    with tf.name_scope("softmax"):
        prediction = tf.nn.softmax(wx_plus_b)


with tf.name_scope('loss'):
    #交叉熵代价函数
    loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=prediction))
    tf.summary.scalar('loss', loss)
with tf.name_scope('train'):
    #使用梯度下降法
    train_step = tf.train.GradientDescentOptimizer(0.5).minimize(loss)


#初始化变量
sess.run(tf.global_variables_initializer())


with tf.name_scope('accuracy'):
    with tf.name_scope('correct_prediction'):
        #结果存放在一个布尔类型的列表中
        #argmax返回一维张量中最大值所在的位置
        correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(prediction, 1))
    with tf.name_scope('accuracy'):
        #求准确率
        #把correct_prediction变为float32类型
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
        tf.summary.scalar('accuracy', accuracy)

#产生metadata文件
if tf.gfile.Exists(DTR + 'projector/metadata.tsv'):
    tf.gfile.DeleteRecursively(DTR + 'projector/metadata.tsv')
with open(DTR + 'projector/metadata.tsv', 'w') as f:
    labels = sess.run(tf.argmax(mnist.test.labels[:], 1))
    for i in range(image_num):
        f.write(str(labels[i]) + '\n')

#合并所有的summary
merged = tf.summary.merge_all()

projector_writer = tf.summary.FileWriter(DTR + 'projector', sess.graph)
save = tf.train.sever()
config = projector.ProjectorConfig()
embed = config.embedding.add()
embed.tensor_name = embedding.name
embed.metadata_path = DTR + 'projector/metadata.tsv'
embed.sprite.image_path = DTR + 'projector/data/mnist_10k_sprite.png'
embed.sprite.single_image_dim.extend([28, 28])
projector.visualize_embeddings(projector_writer, config)


for i in range(max_step):
    #每个批次100个样本
    batch_xs, batch_ys = mnist.train.next_batch(100)
    run_options = tf.RunOptions(trace_level=tf.RunOptions.FULL_TRACE)
    run_metadata = tf.RunMetadata()
    summary, _ = sess.run([merged, train_step], feed_dict={x:batch_xs, y:batch_ys}, options=run_options, run_metadata=run_metadata)
    projector_writer.add_run_metadata(run_metadata, 'step%03d' %i)
    projector_writer.add_summary(summary, i)

    if i % 100 == 0:
        acc = sess.run(accuracy, feed_dict={x:mnist.test.images, y:mnist.test.labels})
        print('Iter' + str(i) + ",Testing Accuracy= " + str(acc))


saver.save(sess, DTR + 'projector/a_model.ckpt', global_step=max_steps)
projector_writer.close()
sess.close()
