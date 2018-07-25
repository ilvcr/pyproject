#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: minimum_spanning_tree_kruskal.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: 2018年07月25日 星期三 22时16分35秒
# Description: 
#************************************************************************#

from __future__ import print_function
num_nodes, num_edges = list(map(int, input().split()))

edges = []

for i in range(num_edges):
    node1, node2, cost = list(map(int, input().split()))
    edges.append((i, node1, nodee2, cost))

edges = sorted(edges, key=lambda edge: edge[3])

parent = [i for i in range(num_nodes)]

def find_parent(i):
    if(i != parent[i]):
        parent[i] = find_parent(parent[i])
    return parent[i]

minumun_spaining_tree_cost = 0
minumun_spaining_tree = []

for edge in edges:
    parent_a = find_parent(edge[1])
    parent_b = find_parent(edge[2])
    if(parent_a != parent_b):
        minumun_spaining_tree_cost += edge[3]
        minumun_spaining_tree.append(edge)
        parent[parent_a] = parent_b

print(minumun_spaining_tree_cost)
for edge in minumun_spaining_tree:
    print(edge)


