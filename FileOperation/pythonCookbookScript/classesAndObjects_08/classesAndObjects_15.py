#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Mon 23 Apr 2018 11:49:41 PM CST
# File Name: classesAndObjects_15.py
# Description:  定义接口或者抽象基类
                    定义一个接口或抽象类，并且通过执行类型检查来确保子类实现了某些特定的方法
"""

#使用 abc 模块可以很轻松的定义抽象基类
from abc import ABCMeta, abstractmethod

class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxbytes=-1):
        pass

    @abstractmethod
    def write(self, data):
        pass


#抽象类的一个特点是它不能直接被实例化, 抽象类的目的就是让别的类继承它并实现特定的抽象方法
class SocketStream(IStream):
    def read(self, maxbytes=-1):
        pass

    def write(self, data):
        pass


#抽象基类的一个主要用途是在代码中检查某些类是否为特定类型，实现特定接口
def serialize(obj, stream):
    if not isinstance(stream, IStream):
        raise TypeError('Expected an IStream')
    pass


#除了继承方式外，还可以通过注册方式来让某个类实现抽象基类
import io

#Register the built-in I/O classes as supporting our interface
IStream.register(io.IOBase)

#Open a normal file and type check
f = open('filename.txt')
isinstance(f, IStream)  #Return True


#@abstractmethod 还能注解静态方法、类方法和 properties 
class A(metaclass=ABCMeta):

    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, value):
        pass

    @classmethod
    @abstractmethod
    def method(cls):
        pass

    @staticmethod
    @abstractmethod
    def method2():
        pass
