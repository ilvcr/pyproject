#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: testdel.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Mar 28 13:08:34 2019
# Description: 
#************************************************************************#


from os.path import join

class FileObject:
    '''
        给文件对象进行包装从而确认在删除文件时文件流关闭
    '''

    def __init__(self, filepath='~', filename='sample.txt'):

        # 读写模式打开一个文件
        self.file = open(join(filepath, filename), 'r+')

    def __del__(self):
        self.file.close()
        del self.file

