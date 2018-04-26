#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Thu 26 Apr 2018 01:19:36 PM CST
# File Name: classesAndObjects_32.py
# Description:  不用递归实现访问者模式

                    使用访问者模式遍历一个很深的嵌套树形数据结构，并且因为超过嵌套层级限制而失败。
                    想消除递归，并同时保持访问者编程模式。


                使用生成器可以在树遍历或搜索算法中消除递归

                利用一个栈和生成器重新实现访问者类
"""

import types

class Node(object):
    pass

class NodeVisitor(object):
    def visit(self, node):
        stack = [node]
        last_result = None
        while stack:
            try:
                last = stack[-1]
                if isinstance(last, types.GeneratorType):
                    stack.append(last.send(last_result))
                    last_result = None
                elif isinstance(last, Node):
                    stack.append(self._visit(stack.pop()))
                else:
                    last_result = stack.pop()
            except StopIteration:
                stack.pop()

        return last_result



    def _visit(self, node):
        methname = 'visit_' + type(node).__name__
        meth = getattr(self, methname, None)
        if meth is None:
            meth = self.generic_visit
        return meth(node)


    def generic_visit(self, node):
        raise RuntimeError('No {} method'.format('visit_ ' + type(node).__name__))




#遍历一个表达式的树
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


#A sample visitor class that evaluates expressions
class Evaluator1(NodeVisitor):#wrong
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
        return - self.visit(node.operand)



class Evaluator2(NodeVisitor):
    def visit_Number(self, node):
        return node.value

    def visit_Add(self, node):
        yield (yield node.left) + (yield node.right)

    def visit_Sub(self, node):
        yield (yield node.left) - (yield node.right)

    def visit_Mul(self, node):
        yield (yield node.left) + (yield node.right)

    def visit_Div(self, node):
        yield (yield node.left) + (yield node.right)

    def visit_Negate(self, node):
        yield - (yield node.operand)


if __name__ == '__main__':
        t1 = Sub(Number(3), Number(4))
        t2 = Mul(Number(2), t1)
        t3 = Div(t2, Number(5))
        t4 = Add(Number(1), t3)
        e = Evaluator1()
        print(e.visit(t4))
