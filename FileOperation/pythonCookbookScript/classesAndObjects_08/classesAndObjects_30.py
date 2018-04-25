#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 25 Apr 2018 11:20:12 PM CST
# File Name: classesAndObjects_30.py
# Description:  实现访问者模式
                    遍历一个树形结构，然后根据每个节点的相应状态执行不同的操作。


                    写一个表示数学表达式的程序
"""


class Node(object):
    pass


class UnaryOperator(Node):
    def __init__(self, operand):
        self.operand = operand


class BinaryOperator(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Add(BinaryOperator):
    pass


class Sub(BinaryOperator):
    pass


class Mul(BinaryOperator):
    pass


class Div(BinaryOperator):
    pass


class Negate(UnaryOperator):
    pass


class Number(Node):
    def __init__(self, value):
        self.value = value


#使用访问者模式支持所有的数字和操作符
class NodeVistor(object):
    def visit(self, node):
        methname = 'visit_' + type(node).__name__
        meth = getattr(self, methname, None)

        if meth is None:
            meth = self.generic_visit

        return meth(node)


    def generic_visit(self, node):
        raise RuntimeError('No {} method'.format('visit_' + type(node).__name__))

#求表达式的值
class Evaluator(NodeVisitor):
    def visit_Number(self, node):
        return node.value


    def visit_Add(self, node):
        return self.visit(node.left) + self.visit(node.right)


    def visit_Sub(self, node):
        return self.visit(node.left) - self.visit(node.right)


    def visit_Mul(self, node):
        return self.visit(node.left) * self.visit(node.right)


    def visit_Div(self, node):
        return self.visit(node.left) / self.visit(node.right)


    def visit_Negate(self, node):
        return -node.operand
