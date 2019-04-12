#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: linklist_creat_and_operation.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Fri Apr 12 11:28:18 2019
# Description: 
#************************************************************************#

class LNode(object):
    #节点初始化函数, p即模拟所存放的下一个节点的地址
    #为了方便传参, 设置p的默认值为0
    def __init__(self, data, p=0):
        self.data = data
        self.next = p

class LinkList(object):
    def __init__(self):
        self.head = None

    #利用尾插法初始化链表
    def init_list(self, data):
        #创建头节点
        self.head = LNode(data[0])
        p = self.head
        #逐个为data内的数据创建节点, 建立链表
        for i in data[1:]:
            node = LNode(i)
            p.next = node
            p = p.next

    #判断链表是否为空
    def is_empty(self):
        if self.head.next == 0:
            print 'Empty list!'
            return 1
        else:
            return 0

    #取链表长度
    def get_linklist_length(self):
        if self.is_empty():
            exit(0)

        p = self.head
        len = 0
        while p:
            len += 1
            p = p.next
        return len

    #遍历链表
    def trave_linklist(self):
        if self.is_empty():
            exit(0)
        print '\rlinklist traving result : '
        p = self.head
        while p:
            print p.data
            p = p.next

    #链表插入数据
    def insert_elem_in_linklist(self, key, index):
        if self.is_empty():
            exit(0)

        if index < 0 or index > self.get_linklist_length() - 1:
            print "\r key error!Program exit."
            exit(0)

        p = self.head
        i = 0
        while i <= index:
            pre = p
            p = p.next
            i += 1

        #遍历找到索引值为index的节点后, 在其后面插入节点
        node = LNode(key)
        pre.next = node
        node.next = p

    #链表删除数据
    def delete_elem_in_linklist(self, index):
        if self.is_empty():
            exit(0)

        if index < 0 or index > self.get_linklist_length() - 1:
            print "\r key error!Program exit."
            exit(0)

        i = 0
        p = self.head

        #遍历找到索引值为index的节点
        while p.next:
            pre = p
            p = p.next
            i += 1
            if i == index:
                pre.next = p.next
                p = None
                return 1

        pre.next = None



