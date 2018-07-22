#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: graph_list.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: 2018年07月22日 星期日 09时30分52秒
# Description: 
#************************************************************************#

from __future__ import print_function

class Graph:
    def __init__(self, vertex):
        self.vertex = vertex
        self.graph = [[0] for i in range(vertex)]

    def add_edge(self):
        self.graph[u-1].qppend(v-1)

    def show(self):
        for i in range(self.vertex):
            print('{}: '.format(i+1), end=' ')
            for j in self.graph[i]:
                print('{}-> '.format(j+1), end=' ')
            print(' ')


g = Graph(100)

g.add_edge(1,3)
g.add_edge(2,3)
g.add_edge(3,4)
g.add_edge(3,5)
g.add_edge(4,5)


g.show()


