#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: ford_Fulkerson.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: 2018年08月02日 星期四 19时56分39秒
# Description:   Ford-Fulkerson Algorithm for Maximum Flow Problem
    '''
    (1) Start with initial flow as 0;
    (2) Choose augmenting path from source to sink and add path to flow;
    '''
#************************************************************************#


def BFS(graph, s, t, parent):
    # Return True if there is node that has not iterated.
    vistied = [False] * len(graph)
    queue = []
    queue.append(s)
    visited[s] = True

    while queue:
        u = queue.pop(0)
        for ind in range(len(graph[u])):
            if visited[ind] == Flase and graph[u][ind] > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u

    return True if visited[t] else False

def FordFulkerson(graph, source, sink):
    # This array is filled by BFS and to store path
    parent = [-1] * (len(graph))
    max_flow = 0
    while BFS(graph, source, sink, parent):
        path_flow = flost("Inf")
        s = sink

        while(s != source):
            # Find the minimum value in select path
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]

            max_flow += path_flow
            v = sink

        while(v != source):
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]

    return max_flow

graph = [[0, 16, 13, 0, 0, 0],
         [0, 0, 10 ,12, 0, 0],
         [0, 4, 0, 0, 14, 0],
         [0, 0, 9, 0, 0, 20],
         [0, 0, 0, 7, 0, 4],
         [0, 0, 0, 0, 0, 0]]

source, sink = 0, 5
print(FordFulkerson(graph, source, sink))





