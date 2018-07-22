#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: breadth_first_search.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: 2018年07月22日 星期日 09时00分51秒
# Description: 
#************************************************************************#

from __future__ import print_function

class Graph(object):
    def __init__(self):
        self.vertex = {}

    #for printing the Graph vertexes
    def printGraph(self):
        for i in self.vertex.keys():
            print(i, ' ->'. ' ->'.join([str(j) for j in self.vertex[i]]))

    #for adding the edge between two vertexes
    def addEdge(self, fromVertex, toVertex):
        # check if vertex is already present,
        if fromVertex in self.vertex.key():
            self.vertex[fromVertex].append(toVertex)
        else:
            #else make a new vertex
            self.vertex[fromVertex] = [toVertex]

    def BFS(self, startVertex):
        # Take a list for stoting already visited vertexes
        visited = [False] * len(self.vertex)

        # create a list to store all the vertexes for BFS
        queue = []

        # mark the source node as visited and enqueue it
        visited[startVertex] = True
        queue.append(startVertex)

        while queue:
            startVertex = queue.pop(0)
            print(startVertex, end = ' ')

            # mark all adjacent nodes as visited and print them
            for i in self.vertex[startVertex]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

if __name__ == '__main__':
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    g.printGraph()
    print('BFS:')
    g.BFS(2)



# OUTPUT:
# 0  ->  1 -> 2
# 1  ->  2
# 2  ->  0 -> 3
# 3  ->  3
# BFS:
# 2 0 3 1



