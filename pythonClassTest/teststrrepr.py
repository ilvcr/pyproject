#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: teststrrepr.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Mar 28 13:21:02 2019
# Description: 
#************************************************************************#

class People(object):

    def __init__(self, name, age):
        # 把属性和对象名绑定在一起，便于访问对象的属性
        self.name = name
        self.age = age
        print 'Create Success'

    #析构函数， 当删除对象时自动删除的方法
    # del  对象或程序执行结束后
    def __del__(self):
        print 'Delete success'    

    # __str__与__repr__都是对对象的字符串显示，使用场景不同
    # 如果没有__str__时，自动调用__repr__方法的内容
    def __str__(self):
        return 'People({},{})'.format(self.name, self.age)

    def __repr__(self):
        return 'People({})'.format(self.name)


if __name__ == '__main__':
    p1 = People('liuchnag', 'age')
    print p1
    print p1.__str__()
