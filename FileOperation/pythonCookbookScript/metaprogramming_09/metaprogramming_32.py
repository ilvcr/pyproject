#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Mon 30 Apr 2018 04:08:09 AM CST
# File Name: metaprogramming_32.py
# Description:  类记录了哪些名字被加载、存储和删除的信息。
"""

import ast

class CodeAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.loaded = set()
        self.stored = set()
        self.deleted = set()


    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Load):
            self.loaded.add(node.id)
        elif isinstance(node.ctx, ast.Store):
            self.stored.add(node.id)
        elif isinstance(node.ctx, ast.Del):
            self.deleted.add(node.id)


#Samole usage
if __name__ == '__main__':
    #Some Python code
    code ='''
    for i in range(10):
        print(i)
    del i
    '''

    #Parse into an AST
    top = ast.parse(code, mode='exec')


    #Feed the AST to analyze name usage
    c = CodeAnalyzer()
    c.visit(top)
    print('Loaded:', c.loaded)
    print('Stored:'. c.stored)
    print('Deleted:', c.deleted)
