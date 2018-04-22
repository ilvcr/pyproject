#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sat 31 Mar 2018 12:36:25 PM CST
# File Name: recongizeImageUseInception-v3.py
# Description:
"""

import tensorflow as tf
import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

class NodeLookup(object):
    def __init__(self):
        label_lookup_path = 'inception_model/imagenet_2012_challenge_label_map_proto.pbtxt'
        uid_lookup_path = 'inception_model/imagenet_synset_to_human_label_map.txt'
        self.node_lookup = self.load(label_lookup_path, uid_lookup_path)

    def load(self, label_lookup_path, uid_lookup_path):
        #加载分类字符串n*********对应分类名称的文件
        proto_as_ascii_lines = tf.gfile.GFile(uid_lookup_path).readlines()
        uid_to_human = {}
        #一行一行得读取数据
        for line in proto_as_ascii_lines:
            #去掉换行符
            line = line.strip('\n')
            parsed_items = line.split('\t')  #按照'\t'分割
            uid= parsed_items[0]  #获取分类编号
            human_string = parsed_items[1]  #获取分类名称
            uid_to_human[uid] = human_string  #保存编号字符串n******与分类名称映射关系

        proto_as_ascii = tf.gfile.GFile(label_lookup_path).readlines()  #加载分类符字符串n***对应分类编号1-1000的文件
        node_id_to_uid = {}
        for line in proto_as_ascii:
            if line.startswith('  target_class:'): 
                target_class = int(line.split(': ')[1])#获取分类编号1-1000
            if line.startswith('  target_class_string:'):
                target_class_string = line.split(': ')[1]#获取编号字符串n****
                node_id_to_uid[target_class] = target_class_string[1:-2]#保存分类编号1-1000与编号字符串n*****映射关系
 

        #建立分类编号1-1000对应分类名称的映射关系
        node_id_to_name = {}
        for key, val in node_id_to_uid.item():
            name = uid_to_human[val]#获取分类名称
            node_id_to_name[key] = name#建立分类编号1-1000到分类名称的映射关系
        return node_id_to_name


    def id_to_string(self, node_id):#传入分类编号1-1000返回分类名称
        if node_id not in self.node_lookup:
            return ''
        return self.node_lookup[node_id]


with tf.gfile.FastGFile('inception_model/classify_image_def.pb', 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    tf.import_graph_def(graph_def, name='')

with tf.Sessiom() as sess:
    softmax_tensor = sess.graph.get_tensor_by_name('softmax:0')
    #遍历目录
    for root, dirs, files in os.walk('images/'):
        for file in files:
            image_data = tf.gfile.FastGFile(os.path.join(root, file), 'rb').read()#载入图片
            predictions = sess.run(softmax_tensor,{'DecodeJpeg/contents:0' : image_data})#图片格式为jpg
            predictions = np.squeeze(predictions)#把结果转为1维数据

            image_path = os.path.join(root, file)#打印图片路径及名称
            print(image_path)
            img = Image.open(image_path)
            plt.imshow(img)
            plt.axis('off')
            plt.show()

            #排序
            top_k = predictions.argsort()[-5:][::-1]
            node_lookup = NodeLookup()
            for node_id in top_k:
                human_string = node_lookup.id_to_string(node_id)#获取分类名称
                score = predictions[node_id]#获取该分类的置信度
                print('%s (score = %.5f)' % (human_string, score))
            print()
